import pywhatkit as pw
txt="""My name Is jaharlal Guchhait
s/d fathers name Milan Chandra Guchhait
live at Rasulpur, District -Hooghly
I am a small farmer and political leader.
I want justice of RG kar Medical College incident."""
pw.text_to_handwriting(txt,"demo1.jpeg",[0,0,138])
print("End")