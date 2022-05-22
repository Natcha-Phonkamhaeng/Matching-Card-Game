from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('400x400+2000+200')

def resize_img(file):
	img = Image.open(file)
	old_width = img.size[0]
	old_height = img.size[1]
	new_width = 100
	new_height = new_width * old_height // old_width
	img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
	card_img = ImageTk.PhotoImage(img)
	return card_img

back_card = resize_img('back_card.png')
two_of_heart = resize_img('two_of_heart.png')
queen = resize_img('queen_of_heart.png')
king = resize_img('king_of_heart.png')


def command(event, b, img):
	b.config(image=img)
	

img1 = Label(root, image=back_card, text='')
img1.grid(row=0, column=0)
img1.bind('<Button-1>', lambda event: command(event, b=img1, img=two_of_heart))

img2 = Label(root, image=back_card, text='')
img2.grid(row=0, column=1)
img2.bind('<Button-1>', lambda event: command(event, b=img2, img=queen))

img3 = Label(root, image=back_card, text='')
img3.grid(row=0, column=2)
img3.bind('<Button-1>', lambda event: command(event, b=img3, img=king))


root.bind('<Escape>', lambda x: root.quit())
root.mainloop()