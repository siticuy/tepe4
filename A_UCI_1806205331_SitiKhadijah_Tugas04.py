# import library PIL dan os
from PIL import Image
import os

def resize(x,y,filename):
    ''' Mengubah ukuran gambar'''
    file,ext = os.path.splitext(filename)   # memisahkan antara nama file dengan ekstensiya (jadi tuple)
    size = x,y                              
    im = Image.open(filename)               # membuka file gambar
    new_im=im.resize(size)                  # mengatur ukuran sesuai input size user
    new_im.save(f'{file}_{size}{ext}')      # menyimpan file yang telah di resize
    im.close()                              # menutup file

def change_ext(filename):
    ''' Mengubah ekstensi gambar'''
    file,ext = os.path.splitext(filename)   # memisahkan antara nama file dengan ekstensiya
    if ext.lower() == '.jpg':               # jika ekstensi file .jpg, diubah ke .png
        im = Image.open(filename)
        im.save(f'{file}_new_ext.png')
        im.close()
    else:                                   # jika ekstensi file .png, diubah ke .jpg
        im = Image.open(filename)
        im.save(f'{file}_new_ext.jpg')      
        im.close()
        
def rotate(angle,filename):
    '''Memutar gambar sesuai angle yang diberikan'''
    im = Image.open(filename)
    im_rotate = im.rotate(angle, expand='True',fillcolor='white')   # expand='False' agar gambar yang di rotate tidak sesuai canvas original
    im_rotate.save(f'{filename}_rotate_{angle}.jpg')
    im.close()

def main():
    os.chdir('C:/Users/USER/Pictures/')                         # mengubah current directory
    print('------------------------------------------\n'
          '---Welcome to simple image edit program---\n'
          '------------------------------------------\n')
    print('the image file only in .jpg or .png')
    
    filename = input('Input your image name[cat1.jpg]: ')       # meminta input nama file
    file, ext = os.path.splitext(filename)                      # split untuk mendapatkan nama file dan ekstensinya
    if ext == '':                                               # jika tidak menuliskan ekstensi file
        print('Be sure to write your extention too')
    elif os.path.exists(filename)==False:                         # mengecek jika file tidak ada di current directory
        print('Your find is not exist in C:/Users/USER/Pictures/\n'
              'Please check your folder\n')
    else:
        if filename[-4:].lower()=='.jpg' or filename[-4:].lower()=='.png':  # ekstensi harus .jpg atau .png
            
            menu = print('1. Resize image \n'
                       '2. Change image ext \n'
                       '3. Rotate image')
            choose = input('What do you choose? ')                          # input user untuk menu yang diinginkan
            if choose == '1':                                               # jika input 1
                inp_size_x = int(input('Input size in pixel, x: '))         
                inp_size_y = int(input('Input size in pixel, y: '))
                resize(inp_size_x,inp_size_y,filename)                      # memanggil fungsi resize untuk dengan x, y, dan nama file dari user
                print('Check your folder to see the resized image')
             
            elif choose == '2':                                             # jika input 2
                menu_ext = print('Choose ext you want :\n'
                               '1. .jpg\n'
                               '2. .png\n')
                choose_ext = input('Choose either 1 or 2: ')            
                if choose_ext == '1' or choose_ext == '2':                  
                    change_ext(filename)                                    # memanggil fungsi change_ext dengan argumen filename user, jika input 1 atau 2
                    print('Check your folder to see the new ext image')
                else:
                    print('Choose only either 1 or 2')                      # jika input selain 2
                
            elif choose == '3':
                inp_angle = int(input('Input angkle to rotate image[ex=90]: '))
                rotate(inp_angle,filename)                                  # memanggil fungsi rotate dengan angle dan filename dari user
                print('Check your folder to see the rotated image')
            else:
                  print('Choose only either 1,2, or 3')                     # untuk input selain 1,2, atau 3
        else:
              print('Your extension must be .png or .jpg')

if __name__=='__main__':
    main()


