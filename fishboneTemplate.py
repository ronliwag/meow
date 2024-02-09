from fpdf import FPDF
#https://www.youtube.com/watch?v=7YS6YDQKFh0
def main():
    fishbone = FPDF('L', 'mm', 'A3')
    fishbone.add_page()
    
    h = 298
    w = 420
    cH = h/8
    cW = w/8
    yGrid = cH
    xGrid = cW
    i = 0
    

    #setting guides
    fishbone.set_draw_color(255, 220, 220)
    fishbone.set_line_width(5)
    
    #horizontal & vertical grids
    while i<8:
        fishbone.line(x1=0,y1=yGrid,x2=w,y2=yGrid)
        fishbone.line(x1=xGrid,y1=0,x2=xGrid,y2=h)
        yGrid+=cH
        xGrid+=cW
        i+=1
    
    #reverting line width and color
    fishbone.set_line_width(1.3)
    fishbone.set_draw_color(0, 0, 0)

    fishbone.set_font('helvetica', size=20)
    fishbone.text(x=5,y=5, txt="Paper: A3, Height = 298mm, Width is 420mm, Cell height = 37.25mm, Cell width = 52.5mm")
    
    #center line and rectangle
    fishbone.line(x1=cW/2, y1=149, x2=w-cW*1.5, y2=149)
    fishbone.rect(x=w-cW*1.5,y=139.5,w=cW*1.3,h=20, style='')
    
    #fishbone branches
    #upper branches
    fishbone.line(x1=w-cW*1.5,y1=h/2,x2=w-cW*2.5,y2=cH)
    fishbone.line(x1=w/2+cW/2,y1=h/2,x2=w/2-cW/2,y2=cH)
    fishbone.line(x1=(w/2-cW*1.5),y1=h/2,x2=(w/2-cW*2.5),y2=cH)
    
    #lower branches
    fishbone.line(x1=(w/2+cW+cW/2),y1=h/2,x2=(w/2+cW/2),y2=h-cH)
    fishbone.line(x1=(w/2-cW),y1=h/2,x2=(w/2-cW*2),y2=h-cH)
    
    #Labels
    #upper
    fishbone.set_font('helvetica', size=30, style='B')
    fishbone.rect(x=cW,y=cH*0.65,w=cW,h=cH/3)
    fishbone.text(x=cW+2, y=cH-2, txt='Materials')
    fishbone.rect(x=cW*3,y=cH*0.65,w=cW+6,h=cH/3)
    fishbone.text(x=cW*3+2, y=cH-2, txt='Equipment')
    fishbone.rect(x=cW*5,y=cH*0.65,w=cW,h=cH/3)
    fishbone.text(x=cW*5+2, y=cH-2, txt='Process')
    #lower
    fishbone.rect(x=cW*1.5,y=cH*7,w=cW,h=cH/3)
    fishbone.text(x=cW*1.5+8, y=cH*7+10, txt='People')
    fishbone.rect(x=cW*4,y=cH*7,w=cW+16,h=cH/3)
    fishbone.text(x=cW*4+2, y=cH*7+10, txt='Environment')
    
    fishbone.output("fishboneTemplate.pdf")

if __name__ == "__main__":
    main()