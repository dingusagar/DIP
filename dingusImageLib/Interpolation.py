class Interpolation:
    @staticmethod
    def nearestNeighbour(img,x,y):
        p,q = int(round(x)),int(round(y))
        return img[q][p]

    @staticmethod
    def bilinear(img,x,y):
        base_x,base_y = math.floor(x),math.floor(y)
        dx,dy = x - base_x , y - base_y
        base_x,base_y = int(base_x),int(base_y)
        next_x,next_y = base_x + 1, base_y + 1

        if next_x > img.shape[1] -1 or next_y > img.shape[0] -1:
            return 0*img.shape[2]
            

        value = (1-dx)*(1-dy)*img[base_y][base_x] + dx*dy*img[base_y+1][base_x+1] +  dx*(1-dy)*img[base_y][base_x+1] + dy*(1-dx)*img[base_y+1][base_x]
        return value
