import json



def get_music(file_path:str = "data.json", music_id: int|None = None) -> list [dict] | dict:
    with open (file_path, "r") as fp:
        musics = json.load(fp)
        if music_id != None and music_id<len(musics):
            return musics [music_id]
        
        return musics
    
def add_music(music: dict, file_path: str = "data.json"):
    musics = get_music(file_path=file_path, music_id=None)
    if musics:
        musics.append(music)
        with open(file_path, "w") as fp:
            json.dump(musics, fp, indent=4, ensure_ascii=False)

#if __name__ == "__main__":
#    print(get_music())