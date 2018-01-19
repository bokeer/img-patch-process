from PIL import Image, ImageDraw, ImageFont 
import os , glob
# get an image
im_syntax = Image.open('source\syntax1.png')
im_function = Image.open('source\\function1.png')
#source_syntax = im_syntax.split()
#print(im_syntax.format ,im_syntax.mode,im_syntax.size)
im_background = Image.open('source\\background.png').convert('RGBA')

#print(im_background.info)
im_line = Image.open('source\line1.png')
im_demo = Image.open('source\demo1.png')
# print('im_background:',im_background.format ,im_background.mode,im_background.size)
# print('im_syntax:',im_syntax.format ,im_syntax.mode,im_syntax.size)
# print('im_function:',im_function.format ,im_function.mode,im_function.size)
# print('im_line:',im_line.format ,im_line.mode,im_line.size)
#im_background.paste(im_syntax,(1000,2800,1000+im_syntax.width,2800+im_syntax.height),mask = source_syntax[3])
#txt.show()
#source_txt[3].show()
#im_background.show()
all_syn_dic = dict()
#per_syn_dic = dict()
def opentextfile():
	try:
		with open('input\syntax.txt', 'r',encoding='utf8') as fr:
			line_state = 0
			for line in fr.readlines():
				#print(line.strip())
				#print(line)
				if line.strip() == '###':
					line_state = 1
					#print('11111111111')
					continue
				if line_state == 1:
					if line.strip() not in all_syn_dic.keys():   #避免重复
						all_syn_dic[line.strip()]={}
						dic_key = line.strip()
						line_state = 2
						continue
					else:
						print(line.strip() +' Error syntax repetitions')
						break
				if (line.strip() == '功能') or (line.strip() == '语法规则') or (line.strip() == 'code'):
					dic_sub_key = line.strip()
					line_state = 3
					continue
				if line_state == 3:
					temp_str = ''
					try:
						temp_str = all_syn_dic[dic_key][dic_sub_key]
					except KeyError as e:
						#print('no key')
						pass
					temp_str += line
					all_syn_dic[dic_key][dic_sub_key]= temp_str
				#print(line)
				# line = line.strip().split('#')
				# dic[line[0]] = line[1]
	except IOError:
		print('file not exist')
opentextfile()
#print(all_syn_dic)

#im_syntax.show()
def textinbox(box,text,fnt,color):   #box[1]==0 高度自适应
	linenum=1
	height=box[1]
	if fnt.getsize(text)[0] > box[0]:
		temp = text
		text_new = ''
		index = 0
		while temp:
			#temp_1=''
			while fnt.getsize(temp[:index])[0] < box[0]:
				index += 1
				if index > len(text):
					break
			if index>0:
				index -=1

			text_new = text_new + temp[:index]+'\n'
			temp = temp[index:]
			linenum += 1
		text=text_new
	if box[1] == 0:
		height = (linenum+1)*fnt.size
		#print('box[1]'+box[1] )
	else:
		if linenum*fnt.size> box[1]:
			height=linenum*fnt.size
			print(text +'box is too small')
	box_temp=(box[0],height)
	text_blank = Image.new('RGBA',box_temp, (255,255,255,0))
	d = ImageDraw.Draw(text_blank)
	d.text((0,0), text, font=fnt, fill=color)
	#print(box_temp)
	#text_blank.show()
	#os.system("pause")
	return text_blank
def textwithcolors(box ,text,eng_fnt,chi_fnt,code_color,num_color,chinese_color):
	text_blank = Image.new('RGBA',box, (255,255,255,0))
	line_height = 40
	d = ImageDraw.Draw(text_blank)
	code_list = text.splitlines()
	#print(code_list)
	y_pos = 0
	tabsize='    '
	for x in code_list:
		x_pos = 0
		if '//' in x:
			x_list=x.split('//')
			x_sub_list =x_list[0].lstrip().split(' ',1)
			#print(len(x_sub_list))
			if len(x_sub_list)==2:
				if '\t' in x_list[0]:
					d.text((x_pos,y_pos), tabsize+x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize(tabsize+x_sub_list[0])[0]
					d.text((x_pos,y_pos),' '+ x_sub_list[1] , font=eng_fnt, fill=num_color)
					x_pos +=eng_fnt.getsize(' '+x_sub_list[1])[0]
				else:
					d.text((x_pos,y_pos), x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize(x_sub_list[0])[0]
					d.text((x_pos,y_pos), ' '+x_sub_list[1] , font=eng_fnt, fill=num_color)
					x_pos +=eng_fnt.getsize(' '+x_sub_list[1])[0]
				#print('2222222')
			else:
				if '\t' in x_list[0]:
					d.text((x_pos,y_pos), tabsize+x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize(tabsize+x_sub_list[0])[0]
				else:
					d.text((x_pos,y_pos), x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize(x_sub_list[0])[0]
			# for y in x_sub_list:
			# 	if '\t' in x_list[0]:
			# 		d.text((x_pos,y_pos), '    '+x_sub_list[pp] , font=eng_fnt, fill=code_color)
			# 		pp += 1
			# 	else:
			# 		d.text((x_pos,y_pos), x_sub_list[pp] , font=eng_fnt, fill=code_color)
			# 		pp += 1
			# print('x_list',x_list)
			# print('x_sub_list',x_sub_list)
			#d.text((x_pos,y_pos), x_list[0], font=eng_fnt, fill=code_color)
			#x_pos +=eng_fnt.getsize(x_list[0])[0]
			# print(eng_fnt.getsize(x_list[0])[0])
			# d.text((x_pos,y_pos), '//', font=eng_fnt, fill=chinese_color)
			# x_pos +=eng_fnt.getsize('//')[0]
			d.text((x_pos,y_pos),'//'+ x_list[1], font=chi_fnt, fill=chinese_color)
			x_pos +=eng_fnt.getsize(x_list[1])[0]
			
		else:
			x_sub_list =x.lstrip().split(' ',1)
			#print(len(x_sub_list))
			if len(x_sub_list)==2:
				if '\t' in x:
					d.text((x_pos,y_pos), '    '+x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize('    '+x_sub_list[0])[0]
					d.text((x_pos,y_pos), ' '+x_sub_list[1] , font=eng_fnt, fill=num_color)
				else:
					d.text((x_pos,y_pos), x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize(x_sub_list[0])[0]
					d.text((x_pos,y_pos), ' '+x_sub_list[1] , font=eng_fnt, fill=num_color)
				#print('2222222')
			else:
				if '\t' in x:
					d.text((x_pos,y_pos), '    '+x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize('    '+x_sub_list[0])[0]
				else:
					d.text((x_pos,y_pos), x_sub_list[0] , font=eng_fnt, fill=code_color)
					x_pos +=eng_fnt.getsize('    '+x_sub_list[0])[0]
			# d.text((x_pos,y_pos), x, font=eng_fnt, fill=code_color)
			# x.lstrip()
			# x_sub_list =x.lstrip().split(' ')
			# print('x'+x)
			# print('x_sub_list',x_sub_list)

			# text = text.expandtabs(tabsize=4)
		y_pos += line_height
	if y_pos < box[1]:
		#print(box[0])
		text_blank =text_blank.crop((0,0,box[0],y_pos))
	else:
		print(text+ '  out box')

	return text_blank

def imgcomposite():
	for infile in glob.glob("input\*.png"):
		file, ext = os.path.splitext(infile)
		im_illustration = Image.open(infile).resize((418,233))
		#im_illustration=im_illustration.rezise(0.75)
		#print(file)
		im_blank = Image.new('RGBA',im_background.size, (255,255,255,0))
		line_pos = 0

		filename=file[6:].upper().strip()
		#syntax_name=filename+' 命令'
		color = (0,0,0,255)
		fnt_1 = ImageFont.truetype('source\Courier.ttf',size=45)
		fnt_2 = ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',size=40)
		text_size_1= fnt_1.getsize(filename)
		text_size_2 = fnt_2.getsize(' 命令')
		# print('text_size_1',text_size_1)
		# print('text_size_2',text_size_2)
		text_demo = textinbox(text_size_1,filename,fnt_1,color)
		x_pos=int((im_background.width-text_size_1[0]-text_size_2[0])/2)
		y_pos=20
		im_blank.paste(text_demo,(x_pos,y_pos,x_pos+text_demo.width,y_pos+text_demo.height),mask = text_demo.split()[3])
		x_pos+=text_size_1[0]
		
		text_demo = textinbox(text_size_2,' 命令',fnt_2,color)
		im_blank.paste(text_demo,(x_pos,y_pos,x_pos+text_demo.width,y_pos+text_demo.height),mask = text_demo.split()[3])
		line_pos = text_demo.height + y_pos-10
		#im_blank.show()
		#print(filename)
		if filename in all_syn_dic.keys():
			#print('yse')
			line_pos += 50
			if '功能' in all_syn_dic[filename].keys():
				fnt = ImageFont.truetype('source\SourceHanSansCN-Regular.otf', size=30)
				text_size = fnt.getsize(all_syn_dic[filename]['功能'])  # 只按一行的空间计算
				# print(all_syn_dic[filename]['功能'])
				# print('text_size')
				# print(text_size)
				x_1_pos = 30
				im_blank.paste(im_function,(x_1_pos,line_pos,x_1_pos+im_function.width,line_pos+im_function.height),mask = im_function.split()[3])
				font_size = 30
				color = (89,87,87,255)
				box = (360,0)
				text_demo =textinbox(box,all_syn_dic[filename]['功能'],fnt,color)
				x_2_pos = 230
				line_pos += 20
				im_blank.paste(text_demo,(x_2_pos,line_pos,x_2_pos+text_demo.width,line_pos+text_demo.height),mask = text_demo.split()[3])
				line_pos += text_demo.height-50
				
				#im_blank.show()
				#text_demo =textinbox(box,all_syn_dic[filename][x],fnt,color)
			else:
				print(filename +'没有功能')
			if '语法规则' in all_syn_dic[filename].keys():
				im_blank.paste(im_line,(200,line_pos ,200+im_line.width,line_pos+im_line.height),mask = im_line.split()[3])
				line_pos += im_line.height-30
				color = (89,87,87,255)
				box = (360,0)
				fnt = ImageFont.truetype('source\SourceHanSansCN-Regular.otf', size=30)
				text_size = fnt.getsize(all_syn_dic[filename]['语法规则'])  # 只按一行的空间计算
				#print(all_syn_dic[filename]['语法规则'])
				#print(text_size)

				x_1_pos = 30
				x_2_pos = 230
				im_blank.paste(im_syntax,(x_1_pos,line_pos,x_1_pos+im_syntax.width,line_pos+im_syntax.height),mask = im_function.split()[3])
				text_demo =textinbox(box,all_syn_dic[filename]['语法规则'],fnt,color)
				line_pos += 20
				im_blank.paste(text_demo,(x_2_pos,line_pos,x_2_pos+text_demo.width,line_pos+text_demo.height),mask = text_demo.split()[3])
				line_pos += text_demo.height
				# im_blank.paste(im_line,(200,line_pos ,200+im_line.width,line_pos+im_line.height),mask = im_line.split()[3])
				# line_pos += im_line.height
				
			else:
				print(filename +'没有语法规则')
			if 'code' in all_syn_dic[filename].keys():
				x_1_pos = 25
				im_blank.paste(im_demo,(x_1_pos,line_pos,x_1_pos+im_demo.width,line_pos+im_demo.height),mask = im_demo.split()[3])
				im_blank.paste(im_illustration,(x_1_pos+91,line_pos+112,x_1_pos+91+im_illustration.width,line_pos+112+im_illustration.height))
				line_pos += im_demo.height
				draw = ImageDraw.Draw(im_blank)
				#draw.line([0, line_pos,im_blank.width,line_pos], fill=(0,0,0,255))
				num_fnt = ImageFont.truetype('source\Courier.ttf', size=28)
				chinese_fnt =ImageFont.truetype('source\SourceHanSansCN-Regular.otf', size=23)
				code_str = all_syn_dic[filename]['code']
				#draw.text((100,line_pos), code_str, font=chinese_fnt, fill=(89,87,87,255))
				im_code=textwithcolors((640,600),code_str,eng_fnt=num_fnt,chi_fnt=chinese_fnt,code_color=(163,125,70,255),num_color=(211,135,83,255),chinese_color=(137,170,60,255))
				im_blank.paste(im_code,(x_1_pos+40,line_pos,x_1_pos+40+im_code.width,line_pos+im_code.height),mask = im_code.split()[3])
				line_pos +=im_code.height
				draw.line([0, line_pos,im_blank.width,line_pos], fill=(0,0,0,255))
				# text_size = fnt.getsize(all_syn_dic[filename]['code'])  # 只按一行的空间计算
				# print(all_syn_dic[filename]['code'])
				# print(text_size)
				# color = (163,125,70,255)
				# box = (600,500)
				# text_demo =textinbox(box,all_syn_dic[filename]['code'],fnt,color)
				# im_blank.paste(text_demo,(60,line_pos+ 25 ,60+box[0],line_pos+ 25 +box[1]),mask = text_demo.split()[3])
				# im_blank.show()
			else:
				print(filename +'miss code')
		else:
			print(all_syn_dic.keys())
			print(filename+'  has no corresponding documents')

		im_blank = im_blank.crop((0,0,im_background.width,line_pos))
		im_background_cut =im_background.crop((0,(im_background.height-line_pos-260),im_background.width,im_background.height))
		im_out = Image.composite( im_blank ,im_background_cut, mask=im_blank.split()[3])
		# im_blank.show()
		# im_background.paste( im_blank ,(0,0,im_blank.width,im_blank.height), mask=im_blank.split()[3])
		out_name=filename+'.png'
		im_out.save('output/'+out_name)
		#im_out.show()
		print(filename+' Done')
imgcomposite()



# text = 'aaaaaabbbbbbffffffff你'
# color = (0,255,0,128)
# box = (360,500)
# font_size = 60
# fnt = ImageFont.truetype('source\SourceHanSansCN-Regular.otf', font_size)
# text_demo =textinbox(box,text,fnt,color)
# text_demo.show()
# im_background.paste(text_demo,(500,500,500+text_demo.width,500+text_demo.height),mask = text_demo.split()[3])
# if text[1:3]:
# 	print('77'+'88')
#d.text((0,font_size*txt_block), text, font=fnt, fill=(0,0,0,128))
#print(fnt.getsize(text))
#source_txt = txt.split()
#txt.show()
#im_background.paste(txt,(10,28,10+txt.width,28+txt.height),mask = source_txt[3])

