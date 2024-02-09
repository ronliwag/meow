from fpdf import FPDF

#preset dimensions for A3 paper
h = 298
w = 420
cH = h/8
cW = w/8

class fishbone(FPDF):
    #displaying grid lines for guide
    def grid(self):
        yGrid = cH
        xGrid = cW
        self.set_draw_color(255, 220, 220)
        self.set_line_width(5)
        i = 0
        while i<8:
            self.line(x1=0,y1=yGrid,x2=w,y2=yGrid)
            self.line(x1=xGrid,y1=0,x2=xGrid,y2=h)
            yGrid+=cH
            xGrid+=cW
            i+=1
        self.set_line_width(1.3)
        self.set_draw_color(0, 0, 0)
    #template itself
    def fishboneTemplate(self):
        self.set_line_width(1.3)
        self.line(x1=cW/2, y1=h/2, x2=w-cW*1.5, y2=149)
        self.rect(x=w-cW*1.5,y=h/2-10,w=cW*1.3,h=20, style='')
        self.line(x1=w-cW*1.5,y1=h/2,x2=w-cW*2.5,y2=cH)
        self.line(x1=w/2+cW/2,y1=h/2,x2=w/2-cW/2,y2=cH)
        self.line(x1=(w/2-cW*1.5),y1=h/2,x2=(w/2-cW*2.5),y2=cH)
        self.line(x1=(w/2+cW+cW/2),y1=h/2,x2=(w/2+cW/2),y2=h-cH)
        self.line(x1=(w/2-cW),y1=h/2,x2=(w/2-cW*2),y2=h-cH)
        self.set_font('helvetica', size=30, style='B')
        self.rect(x=cW,y=cH*0.65,w=cW,h=cH/3)
        self.text(x=cW+2, y=cH-2, txt='Materials')
        self.rect(x=cW*3,y=cH*0.65,w=cW+6,h=cH/3)
        self.text(x=cW*3+2, y=cH-2, txt='Equipment')
        self.rect(x=cW*5,y=cH*0.65,w=cW,h=cH/3)
        self.text(x=cW*5+4, y=cH-2, txt='Process')
        self.rect(x=cW*1.5,y=cH*7,w=cW,h=cH/3)
        self.text(x=cW*1.5+8, y=cH*7+10, txt='People')
        self.rect(x=cW*4,y=cH*7,w=cW+16,h=cH/3)
        self.text(x=cW*4+2, y=cH*7+10, txt='Environment')

def main():
    sample = fishbone('L','mm','A3')
    sample.add_page()
    #sample.grid()
    sample.fishboneTemplate()
    sample.output('fishbone.pdf')
    
if __name__ == "__main__":
    main()