import blowfish
import sqlite3
import json
from datetime import datetime

def decrypt(inputFile, key="JSTMUSIC_2"):
    f = open(inputFile, "rb")
    ciphertext = f.read()
    f.close()


    cipher = blowfish.Cipher(bytes(key, 'utf-8'))

    data_decrypted = b"".join(cipher.decrypt_ecb(ciphertext))

    f = open(inputFile + '.db', "wb")
    ciphertext = f.write(data_decrypted)
    f.close()

def convertToJson(inputFile):
    # Connect to the database
    conn = sqlite3.connect(inputFile)
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM TABLE_SONGS")

    # Fetch column names and rows
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    return(data)

def format(musicoletData):
    formatedData = []
    for song in musicoletData:
        formatedData.extend([{
            "endTime" : datetime.now().strftime("%Y-%m-%d %H:%M"),
            "artistName" : song["COL_ARTIST"].split("/")[0],
            "trackName" : song["COL_TITLE"],
            "msPlayed" : song["COL_DURATION"]
        }]*song["COL_NUM_PLAYED"])
    return(formatedData)

def save(data, name="FormatedStreamingHistory.json"):
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

decrypt("DB_SONGS_LOG")
data = convertToJson("DB_SONGS_LOG.db")
data = format(data)
save(data, "FormatedStreamingHistory.json")