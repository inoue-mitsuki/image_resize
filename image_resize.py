import os
from glob import glob
from PIL import Image

def resize(rename):

  for dir_name in all_dir:
    #リサイズする拡張子を指定
    extensions = ["/*.jpg", "/*.jpeg", "/*.png"]
    files = []
    #リサイズするデータをリストに入れる
    for extension in extensions:
      files.extend(glob(path + dir_name + extension))
    #resize
    for f in files:
      img = Image.open(f)
      #画像サイズを半分にする
      img_resize = img.resize((int(img.width/2), int(img.height/2)))
      if rename == "はい":
        #ファイル名と拡張子をわける
        ftitle, fext = os.path.splitext(f)
        img_resize.save(ftitle + '_half' + fext)
      else:
        img_resize.save(ftitle + fext)

#リサイズするフォルダを指定
path = ("./")
#path直下のフォルダ名、ファイル名を取得
all_file = os.listdir(path)
#ファイル名のみにする
all_dir = [f for f in all_file if os.path.isdir(os.path.join(path, f))]

save_name = input("別名保存にしますか？(はい or いいえ)> ")
if save_name == "はい":
  resize(save_name)
  input("処理が完了しました。元の名前 + halfという名前で保存されています。Enterを押してください。")

elif save_name == "いいえ":
  resize(save_name)
  input("処理が完了しました。Enterを押してください。")
else:
  input("はい or いいえで入力してください。処理を終了します。Enterを押してください。")
