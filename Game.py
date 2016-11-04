#Connor Price ETGG1801 51 Assignment 7
import pygame
import random
import time
pygame.init()
ds=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)
px=400
py=300
ps=1
score=0
coin=0
ob_count=0
ob_size=75
player_size=25
ob_box=ob_size+player_size
cx=random.randint(30,770)
cy=random.randint(30,570)
ox=random.randint(50,750)
oy=random.randint(50,550)
font=pygame.font.SysFont("Bauhaus 93",26)
timer=60
start_time=time.time()
def draw_player(animation):
    pygame.draw.circle(ds,(200,200,150),(px,py),player_size,0)#head
    if animation<100:
        pygame.draw.circle(ds,(255,255,255),(px-10,py-10),5,0)#eyes
        pygame.draw.circle(ds,(255,255,255),(px+10,py-10),5,0)
        pygame.draw.circle(ds,(0,0,255),(px-10,py-10),2,0)#pupils
        pygame.draw.circle(ds,(0,0,255),(px+10,py-10),2,0)
    else:
        pygame.draw.circle(ds,(200,200,150),(px-10,py-10),5,0)#blink
        pygame.draw.circle(ds,(200,200,150),(px+10,py-10),5,0)
    pygame.draw.line(ds,(0,0,0),(px-10,py+15),(px+10,py+15),2)#mouthas
    if coin_dist <=200:
        pygame.draw.line(ds,(0,0,0),(px-10,py+15),(px+10,py+15),2)
        pygame.draw.line(ds,(0,0,0),(px-10,py+15),(px-20,py+10),2)
        pygame.draw.line(ds,(0,0,0),(px+10,py+15),(px+20,py+10),2)
    pygame.draw.polygon(ds,(0,0,0),[(px,py-5),(px-10,py+5),(px+10,py+5)],2)#nose    
    pygame.draw.circle(ds,(0,0,0),(px-5,py+4),3,0)
    pygame.draw.circle(ds,(0,0,0),(px+6,py+4),3,0)
def draw_coin(cx,cy,animation):
    if animation<100:
        pygame.draw.circle(ds,(255,255,0),(cx,cy),25,0)
    else:
        pygame.draw.circle(ds,(255,255,255),(cx,cy),25,0)#shine
    pygame.draw.line(ds,(50,50,50),(cx-5,cy+20),(cx-5,cy-20),2)
    pygame.draw.line(ds,(50,50,50),(cx+5,cy+20),(cx+5,cy-20),2)
    pygame.draw.line(ds,(50,50,50),(cx-10,cy-15),(cx+10,cy-15),2)
    pygame.draw.line(ds,(50,50,50),(cx-10,cy-15),(cx-10,cy+15),2)
    pygame.draw.line(ds,(50,50,50),(cx-10,cy+15),(cx+10,cy+15),2)
def clear_screen():
    pygame.draw.rect(ds,(0,0,0),(0,0,800,600,),0)
while True:
    pygame.event.pump()
    mouse_x,mouse_y=pygame.mouse.get_pos()
    ks=pygame.key.get_pressed()
    (m_lb,m_mb,m_rb)=pygame.mouse.get_pressed()
    if ks[pygame.K_ESCAPE]==True:
        break
    cdx=px-cx
    cdy=py-cy
    odx=px-ox
    ody=py-oy
    codx=cx-ox
    cody=cy-oy
    ob_dist=(odx**2+ody**2)**.5
    coin_dist=(cdx**2+cdy**2)**.5
    coin_ob_dist=(codx**2+cody**2)**.5
    draw_player(random.randint(0,100))
    if ks[pygame.K_w]==True:
        py-=1
    if ks[pygame.K_s]==True:
        py+=1
    if ks[pygame.K_a]==True:
        px-=1
    if ks[pygame.K_d]==True:
        px+=1
    if px>775:
        px=775
    if px<25:
        px=25
    if py>575:
        py=575
    if py<25:
        py=25
    if cx>775:
        cx=775
    if cx<25:
        cx=25
    if cy>575:
        cy=575
    if cy<25:
        cy=25
    if ox>800-ob_size:
        ox=800-ob_size
    if ox<0+ob_size:
        ox=0+ob_size
    if oy>600-ob_size:
        oy=600-ob_size
    if oy<0+ob_size:
        oy=0+ob_size
    draw_coin(cx,cy,random.randint(0,100))
    if coin_dist<50:
        pygame.draw.circle(ds,(0,0,0),(cx,cy),25,0)
        cx=random.randint(30,770)
        cy=random.randint(30,570)
        draw_coin(cx,cy,random.randint(0,100))
        ox=random.randint(50,750)
        oy=random.randint(50,550)
        pygame.draw.circle(ds,(255,255,255),(ox,oy),ob_size,0)#obstacle
        score+=1
    font_surf1=font.render("Score:"+str(score),0,(255,255,255),(0,0,0))
    font_surf2=font.render("Time:"+str(timer),0,(255,255,255),(0,0,0))
    count=time.time()-start_time
    if timer>.0001:
        timer-=count
    ds.blit(font_surf1,(0,0))
    ds.blit(font_surf2,(680,0))
    start_time=time.time()
    cx+=random.randint(-1,1)
    cy+=random.randint(-1,1)
    ox+=random.randint(-1,1)
    oy+=random.randint(-1,1)
    pygame.draw.circle(ds,(255,255,255),(ox,oy),ob_size,0)#obstacle
    if ob_dist<=ob_box and px<ox:
        px-=1
    if ob_dist<=ob_box and px>ox:
        px+=1
    if ob_dist<=ob_box and py<oy:
        py-=1
    if ob_dist<=ob_box and py>oy:
        py+=1
    if coin_ob_dist<ob_box and cx<ox:
        cx-=1
    if coin_ob_dist<ob_box and cx>ox:
        cx+=1
    if coin_ob_dist<ob_box and cy<oy:
        cy-=1
    if coin_ob_dist<ob_box and cy>oy:
        cy+=1
    pygame.display.flip()
    clear_screen()
    if timer<=0:
        font_surf3=font.render("GAME OVER",0,(255,0,0),(0,0,0))
        ds.blit(font_surf3,(400-font_surf3.get_width()//2,300-font_surf3.get_height()//2))
        font_surf4=font.render("FINAL SCORE:"+str(score),0,(255,255,255),(0,0,0))
        ds.blit(font_surf4,(400-font_surf4.get_width()//2,325-font_surf4.get_height()//2))
        pygame.display.flip()
        time.sleep(3)
        break
print("Final Score:",score)
pygame.quit()

