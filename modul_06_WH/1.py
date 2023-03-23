def sorting_files_into_folders(data):
    """Sorting files into folders"""
    images = {}
    video = {}
    documents = {}
    audio = {}
    archives = {}
    unknown_extensions = {}
    print(len(data))

    for key, file_info in data.items():
        file_extension = file_info.extension
        if file_extension.upper() in IMAGES_EXTENSIONS:
            images[key] = ['images', file_info]

        elif file_extension.upper() in VIDEO_EXTENSIONS:
            video[key] = ['video', file_info]

        elif file_extension.upper() in DOCUMENTS_EXTENSIONS:
            documents[key] = ['documents', file_info]

        elif file_extension.upper() in AUDIO_EXTENSIONS:
            audio[key] = ['audio', file_info]

        elif file_extension.upper() in ARCHIVES_EXTENSIONS:
            print('=', file_info.name, file_info.extension)
            archives[key] = ['archives', file_info]

        else:
            unknown_extensions[key] = file_info
    folders = [images, video, documents, audio, archives, unknown_extensions]

    return folders

if __name__ == '__main__':
    IMAGES_EXTENSIONS = ['.JPEG', '.PNG', '.JPG', '.SVG', '.IMG']
    VIDEO_EXTENSIONS = ['.AVI', '.MP4', '.MOV', '.MKV', '.FLV']
    DOCUMENTS_EXTENSIONS = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
    AUDIO_EXTENSIONS = ['.MP3', '.OGG', '.WAV', '.AMR']
    ARCHIVES_EXTENSIONS = ['.ZIP', '.GZ', '.TAR', '.RAR']
    
в функцію приходять такі данні : {140142947190960: InfoFile(name='UTC--2017-02-02T12-58-56', extension='.250137100Z--f68c5eda68ade011021cbcea137f1447947c2aaf', path='/home/alex/Desktop/garbage/ReWalet', old_path=None), 140142947192880: InfoFile(name='Non-WHQL-Win10-64Bit-Radeon-Software-Crimson-16.9.2-Sep21.exe_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage/Razgon', old_path=None), 140142966552848: InfoFile(name='BONES - BiggestLetdown [ZAKACHAI1.RU].mp3_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage', old_path=None), 140142947443504: InfoFile(name='PolarisBiosEditor', extension='.exe', path='/home/alex/Desktop/garbage/Razgon/PolarisBiosEditor-master', old_path=None), 140142947443584: InfoFile(name='vc_redist.x64', extension='.exe', path='/home/alex/Desktop/garbage/Dwarf', old_path=None), 140142947536624: InfoFile(name='$RNR1HRX', extension='.bat', path='/home/alex/Desktop/garbage/Batniki/New folder', old_path=None), 140142947536688: InfoFile(name='$R8TFGL7', extension='.bat', path='/home/alex/Desktop/garbage/Batniki/New folder', old_path=None), 140142947536752: InfoFile(name='$RTD5223', extension='.bat', path='/home/alex/Desktop/garbage/Batniki/New folder', old_path=None), 140142947536816: InfoFile(name='$RL994IR', extension='.bat', path='/home/alex/Desktop/garbage/Batniki/New folder', old_path=None), 140142947443664: InfoFile(name='Etc+Pasc_EM_NP', extension='.bat', path='/home/alex/Desktop/garbage/Batniki', old_path=None), 140142947443744: InfoFile(name='Eth+Dcr_CT_SN', extension='.bat', path='/home/alex/Desktop/garbage/Batniki', old_path=None), 140142947443824: InfoFile(name='Eth+Dcr_DP_SN', extension='.bat', path='/home/alex/Desktop/garbage/Batniki', old_path=None), 140142947262720: InfoFile(name='Non-WHQL-Win10-64Bit-Radeon-Software-Crimson-16.9.2-Sep21', extension='.exe', path='/home/alex/Desktop/garbage/Razgon', old_path=None), 140142947235472: InfoFile(name='atiflash_274.zip_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage/Razgon', old_path=None), 140142947235568: InfoFile(name='USBdriver_TSHARK28_W14.41.5.rar_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage/Alfa 5', old_path=None), 140142947235664: InfoFile(name='UPGRADEDOWNLOAD_R2.9.9015.rar_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage/Alfa 5', old_path=None), 140142946854704: InfoFile(name='Release_1.0.0.4.zip_Zone', extension='.Identifier', path='/home/alex/Desktop/garbage', old_path=None), 140142947444944: InfoFile(name='ATIWinflashcht', extension='.dll', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947537840: InfoFile(name='atikia64', extension='.sys', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947537904: InfoFile(name='ATIWinflash', extension='.exe', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947445024: InfoFile(name='ethminer-ethereumpool', extension='.bat', path='/home/alex/Desktop/garbage/Dwarf/eth', old_path=None), 140142947537968: InfoFile(name='atillk64', extension='.sys', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947538096: InfoFile(name='eth-proxy', extension='.conf', path='/home/alex/Desktop/garbage/Dwarf/eth-proxy', old_path=None), 140142947538160: InfoFile(name='PackageType', extension='.Dat', path='/home/alex/Desktop/garbage/Win10_64Bit_Crimson_ReLive_17.10.2_Oct23/Config', old_path=None), 140142947445104: InfoFile(name='ATIWinflashsve', extension='.dll', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947445184: InfoFile(name='ATIWinflashita', extension='.dll', path='/home/alex/Desktop/garbage/Razgon/atiflash_274', old_path=None), 140142947445264: InfoFile(name='Settings.Designer', extension='.cs', path='/home/alex/Desktop/garbage/Razgon/PolarisBiosEditor-master/Properties', old_path=None), 140142947445344: InfoFile(name='ethminer-ethpool', extension='.bat', path='/home/alex/Desktop/garbage/Dwarf/eth', old_path=None)}


якщо декілька разів прогнати данні через функцію то вона все відфільтровує