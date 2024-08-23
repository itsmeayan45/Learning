import pywhatkit as pw
txt="""My name Is Xamp
s/d fathers name samc
live at dfgh, District -fghj
I am a small farmer and political leader.
I want justice of RG kar Medical College incident."""
pw.text_to_handwriting(txt,"demo1.jpeg",[0,0,138])
print("End")