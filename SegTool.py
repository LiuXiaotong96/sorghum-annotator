import numpy as np
from PIL import Image
import queue as Queue
from matplotlib.nxutils import points_inside_poly

class SegTool:
             
    def magicwand(im,click_x,click_y,threshold,ID=0,mode='new',is_nei=False,queue = None,pointmap = None):
        checkmap = np.zeros(im.shape)
        checkmap[click_x,click_y] = 8;
        #pointlist = Queue.Queue();
        #pointlist.put([click_x,click_y]);
        newpointmap = np.zeros(im.shape)
        if pointmap is None:
            pointmap = np.zeros(im.shape)
        pointmap.astype(int)
        if queue is None:
            queue = Queue.Queue();
            queue.put([click_x,click_y]);
        while (not queue.empty()):
            center = queue.get();
            neighbour = SegTool.getneighbourpixel(pointmap,center[0],center[1],mode);
            modepoint=True;
            if mode=='add' or mode=='new':
                modepoint=True;
            else:
                modepoint=False;
            for i in range(0,len(neighbour)):
                if checkmap[neighbour[i][0],neighbour[i][1]] < 8:
                    diff=0;
                    if is_nei:
                        diff = abs(im.item((center[0],center[1]))-im.item((neighbour[i][0],neighbour[i][1])));
                    else:
                        diff = abs(im.item((click_x,click_y))-im.item((neighbour[i][0],neighbour[i][1])));
                    if diff<threshold and ((modepoint and pointmap.item((neighbour[i][0],neighbour[i][1]))==0) or (not modepoint and pointmap.item((neighbour[i][0],neighbour[i][1]))==ID)):
                        queue.put(neighbour[i]);
                        x = neighbour[i][0]
                        y = neighbour[i][1]
                        newpointmap[x][y]=1;
                        checkmap[neighbour[i][0],neighbour[i][1]] = 7;    
                    checkmap[neighbour[i][0], neighbour[i][1]] = checkmap[neighbour[i][0], neighbour[i][1]] + 1;
        if mode=='new':
            pointmap=pointmap+newpointmap*(ID);
        elif mode=='add':
            pointmap=pointmap+newpointmap*(ID);
        else:
            pointmap=pointmap-newpointmap*(ID);    
        return pointmap
    
    def getneighbourpixel(mask_map, x, y, mode):
        neighbour=[];
        size = mask_map[:,:,0].shape;
        width = size[0];
        height = size[1];   
        if x > 1 and x < width-1 and y > 1 and y < height-1:
            for i in range(-1,2):
                for j in range(-1,2):
                    if i == 0 and j == 0:
                        continue;
                    if (mode=='new' or mode=='add') and mask_map[:,:,0][x+i][y+j] == 0:
                        neighbour.append([x+i,y+j])
                    if mode=='minus' and mask_map[:,:,0][x+i][y+j] == mask_map.max():
                        neighbour.append([x+i,y+j])
        return neighbour 
        
    def select_Region(mask_map,x,y):
        region=mask_map[x,y];
        mask_map[mask_map!=region]=0;
        mask_map[mask_map!=0]=1;
        return mask_map;
        
    def draw_Polygon(mask_map,x1,y1,x2,y2,x3,y3,x4,y4):
        [nx,ny] = mask_map.shape;
        poly_verts = [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x1,y1)]
        x,y = np.meshgrid(np.arange(nx), np.arange(ny))
        x, y = x.flatten(), y.flatten()
        points = np.vstack((x,y)).T
        grid = points_inside_poly(points, poly_verts)
        grid = grid.reshape((nx,ny))
        grid = 1*grid;
        return grid
        
    
    def find_Line(im,x1,y1,x2,y2,threshold):
        points = SegTool.get_line(x1,y1,x2,y2)
        slope = abs(im[x1][y1] - im[x2][y2])/np.sqrt(np.sum((np.asarray([x1,y1]) - np.asarray([x2,y2]))**2))
        result = Queue.Queue();
        while(not points.empty()):
            a = points.get();
            if a==[x1,y1]:
                continue;
            if abs(abs(im[x1][y1] - im[a[0]][a[1]])/np.sqrt(np.sum((np.asarray([x1,y1]) - np.asarray(a))**2))-slope)<threshold:
                result.put(a);
        return result

    def get_line(x1, y1, x2, y2):
        points = Queue.Queue();
        issteep = abs(y2-y1) > abs(x2-x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2-y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.put([y, x])
            else:
                points.put([x, y])
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        return points
    
    def new_stem(im,click_x1,click_y1,click_x2,click_y2,threshold,stemthreshold,ID=0,mode = 'new',is_nei =False,pointmap = None):
        pointqueue=SegTool.find_Line(im,click_x1,click_y1,click_x2,click_y2,stemthreshold)
        return SegTool.magicwand(im,click_x1,click_y1,threshold,ID,mode,is_nei,pointqueue,pointmap = None)

    def add_stem(im,click_x1,click_y1,click_x2,click_y2,threshold,stemthreshold,ID=0,mode = 'add',is_nei =False,pointmap = None):
        pointqueue=SegTool.find_Line(im,click_x1,click_y1,click_x2,click_y2,stemthreshold)
        return SegTool.magicwand(im,click_x1,click_y1,threshold,ID,mode,is_nei,pointqueue,pointmap = None)
        
    def minus_stem(im,click_x1,click_y1,click_x2,click_y2,threshold,stemthreshold,ID=0,mode = 'minus',is_nei =False,pointmap = None):
        pointqueue=SegTool.find_Line(im,click_x1,click_y1,click_x2,click_y2,stemthreshold)
        return SegTool.magicwand(im,click_x1,click_y1,threshold,ID,mode,is_nei,pointqueue,pointmap = None)
        
    def find_stem(im,x1,y1,x2,y2,x3,y3,x4,y4,ID=0):
        return draw_Polygon(im,x1,y1,x2,y2,x3,y3,x4,y4)*ID;

    def new_leaf(im,click_x,click_y,threshold,ID=0,mode='new',is_nei=False,pointmap = None):
        return magicwand(im,click_x,click_y,threshold,ID,mode,is_nei,queue = None, pointmap=pointmap)
    
    def add_leaf(im,click_x,click_y,threshold,ID=0,mode='add',is_nei=False,pointmap = None):
        return magicwand(im,click_x,click_y,threshold,ID,mode,is_nei,queue = None, pointmap=pointmap)

    def minus_leaf(im,click_x,click_y,threshold,ID=0,mode='minus',is_nei=False,pointmap = None):
        return magicwand(im,click_x,click_y,threshold,ID,mode,is_nei,queue = None, pointmap=pointmap)
