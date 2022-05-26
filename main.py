from tkinter import Scrollbar
from PIL import Image, ImageTk
import PySimpleGUI as sg
import io
import os
from numpy import pad



# get img data used ImageTk(Tkinter based)
def get_img(path=r'data\image\EMPTY.png', maxsize=(640,360), first=False):

    img = Image.open(path)
    img.thumbnail(size=maxsize)
    if first:
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

    return ImageTk.PhotoImage(img)
    


#==========================================MAIN================================================

#define Variables

extension = '.png' #file extension. Default -> PNG
img_path = 'example.png'
dir_path = 'none'
file_name = 'example'


# define layout -------------------------------------------------------------------------------
img_zone = sg.Frame('', 
                    [
                        [sg.Image(data=get_img(first=True), 
                                  key='img_thum')]
                    ], 
                    size=(650,370)
                    )


convs = sg.Frame(' 変換拡張子 ',
                    [
                    [sg.Text('選択中：'), sg.Text(extension, key='ext',background_color='black')],
                    [sg.Button('BMP'), sg.Button('DIB')],
                    [sg.Button('EPS'), sg.Button('GIF')],
                    [sg.Button('ICO'), sg.Button('IM')],
                    [sg.Button('PPM'), sg.Button('SGI')],
                    [sg.Button('TGA'), sg.Button('TIFF')],
                    [sg.Button('JPEG'), sg.Button('PCX')],
                    [sg.Button('JPEG2000'), sg.Button('PNG')],
                    [sg.Button('PDF'), sg.Button('WebP')]
                    ]
                    , vertical_alignment='t',size=(300,370)
                )


output_frame = sg.Frame('',
                        [
                        [sg.ProgressBar(100,
                                        orientation='h',
                                        size=(97,15),
                                        pad=((5,5),(10,0)),
                                        key='bar')],

                        [sg.Output(size=(150,6),
                                   pad=((5,5),(10,5)),
                                   text_color='white',
                                   background_color='black',
                                   key='output')]
                        ], 

                        pad=((5,5),(5,10)),size=(810,140)
                        )


layout = [  
            [sg.Text('''  1. 元画像を選択     2. 保存先を選択     3. 保存ファイル名を入力     4. 拡張子を選択     5. 変換開始ボタン押下  ''')],
            
            [sg.Text('  元画像  '), 
             sg.InputText(key='file1',
                          enable_events=True,
                          default_text='画像のパスを入力'),
             sg.FileBrowse(' 参照 ')],

            [sg.Text('  保存先  '),
             sg.InputText(key='folder1',
                          enable_events=True,
                          default_text='保存先フォルダのパスを入力'),
             sg.FolderBrowse(' 参照 ')],

            [sg.Text('  保存名  '),
             sg.InputText(key='save_name',
                          default_text='保存するファイル名を入力')],

            [img_zone, convs],

            [sg.Button('  変換開始  ')],

            [output_frame]
        ]

#-----------------------------------------------------------------------------------------------


sg.theme('DarkBlue') #PySimpleGUI テーマ選択



window = sg.Window('画像変換君1号 － 試作型',
                    layout,
                    size=(835,690),
                    #resizable=True
                  )


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


    elif event == 'file1':
        img_path = values['file1']
        try:
            window['img_thum'].update(data=get_img(path=img_path))
            dir_path = os.path.dirname(img_path)
            window['folder1'].update(dir_path)
            window['save_name'].update(os.path.basename(img_path).split('.', 1)[0] + '_conv')
            print('画像選択： ', img_path)
        except:
            print('ERROR：' + img_path + 'を読み込めませんでした')
            window['file1'].update('画像のパスを入力')
            img_path = 'example.png'


    elif event == 'folder1':
        dir_path = values['folder1']
        print('保存先選択： ', dir_path)
    

    elif event == '  変換開始  ':
        saves = dir_path + '/' + values['save_name'] + extension
        ans = sg.popup_ok_cancel('現在の設定で変換しますか？\n\n' + img_path + '\n\nから\n\n' + saves + '\n')
        if ans == 'OK':
            try:
                img = Image.open(img_path).convert('RGB')
                img.save(saves)
                print(saves + 'を保存しました')
            except:
                print('ERROR：' + saves + 'を保存できませんでした')
        else:
            continue
    

    elif event == 'BMP':
        extension = '.bmp'
        print('変換対象拡張子：BMPを選択')
    elif event == 'DIB':
        extension = '.dib'
        print('変換対象拡張子：DIBを選択')
    elif event == 'EPS': # cannot Load 
        extension = '.eps'
        print('変換対象拡張子：EPSを選択')
    elif event == 'GIF':
        extension = '.gif'
        print('変換対象拡張子：GIFを選択')
    elif event == 'ICO':
        extension = '.ico'
        print('変換対象拡張子：ICOを選択')
    elif event == 'IM':
        extension = '.im'
        print('変換対象拡張子：IMを選択')
    elif event == 'PCX':
        extension = '.pcx'
        print('変換対象拡張子：PCXを選択')
    elif event == 'PPM':
        extension = '.ppm'
        print('変換対象拡張子：PPMを選択')
    elif event == 'SGI':
        extension = '.sgi'
        print('変換対象拡張子：SGIを選択')
    elif event == 'TGA':
        extension = '.tga'
        print('変換対象拡張子：TGAを選択')
    elif event == 'TIFF':
        extension = '.tif'
        print('変換対象拡張子：TIFFを選択')
    elif event == 'JPEG':
        extension = '.jpg'
        print('変換対象拡張子：JPEGを選択')
    elif event == 'JPEG2000':
        extension = '.jp2'
        print('変換対象拡張子：JPEG2000を選択')
    elif event == 'PNG':
        extension = '.png'
        print('変換対象拡張子：PNGを選択')
    elif event == 'PDF': # cannot Load
        extension = '.pdf'
        print('変換対象拡張子：PDFを選択')
    elif event == 'WebP':
        extension = '.webp'
        print('変換対象拡張子：WebPを選択')
    
    window['ext'].update(extension)
    

window.close()
