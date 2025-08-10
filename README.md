# Musicolet Playback History Decryptor & Formatter

This Python script decrypts **Musicolet Music Player**’s playback log database, extracts song play history, and converts it into a **Spotify-style streaming history JSON** format.

## 📌 Features

*   **Decrypt** Musicolet’s encrypted `DB_SONGS_LOG` file (Blowfish ECB).
    
*   **Read & parse** song playback logs from the SQLite database.
    
*   **Format** entries to match Spotify’s `StreamingHistory.json` style.
    
*   **Export** the result as a nicely formatted `.json` file.
    

## ⚙️ Requirements

Make sure you have Python 3.x installed and the following package:


`pip install blowfish`

    

## 🚀 Usage

1.  **Get** your Musicolet `DB_SONGS_LOG` file by going into your musicolet settings -> Backup/Restore -> Backup Now
    
    from the zip file, copy the `DB_SONGS_LOG` file into the same folder as the script
    
2.  **Run** the script:
    
    `python main.py`
    
3.  The script will:
    
    *   Create a decrypted file: `DB_SONGS_LOG.db`
        
    *   Convert it into a formatted JSON file: `FormatedStreamingHistory.json`
        

## 📝 Output Format

The output JSON will look like this:

json

CopyEdit

`[     {         "endTime": "2025-08-10 14:35",         "artistName": "Artist Name",         "trackName": "Song Title",         "msPlayed": 210000     },     ... ]`

*   `endTime` — The timestamp of when the script was run (Musicolet does not store exact play end times).
    
*   `artistName` — The first artist listed for the song.
    
*   `trackName` — The song title.
    
*   `msPlayed` — The track duration in milliseconds.
    
*   Each play is repeated in the JSON for `COL_NUM_PLAYED` times.
    

## ⚠️ Notes

*   The script uses a hardcoded **Blowfish key** (`JSTMUSIC_2`) — this is the key Musicolet uses to encrypt its log database.
    
*   The database table **`TABLE_SONGS`** is assumed to be present in `DB_SONGS_LOG.db`.

## LICENSE
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.