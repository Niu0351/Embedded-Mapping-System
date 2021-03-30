import numpy as np
import open3d as o3d
import serial
import math

if __name__=="__main__":

    s = serial.Serial("COM10", 115200)
    print("Opening: " + s.name)
    
    f = open("demofile.xyz", "w")
    cnt=0;
    x=0.0;
    while True:
        for i in range(8):
            r=s.readline()
            c=r.decode()
            if c == "Stop\n":
                break
            print(c)
            d=float(str(c))
            
            if i==0:
                f.write('%f 0 %f\n' % (x, -d))
            if i==1:
                f.write('%f %f %f\n' % (x, d/math.sqrt(2), -d/math.sqrt(2)))
            if i==2:
                f.write('%f %f 0\n' % (x, d))
            if i==3:
                f.write('%f %f %f\n' % (x, d/math.sqrt(2), d/math.sqrt(2)))
            if i==4:
                f.write('%f 0 %f\n' % (x, d))
            if i==5:
                f.write('%f %f %f\n' % (x, -d/math.sqrt(2), d/math.sqrt(2)))
            if i==6:
                f.write('%f %f 0\n' % (x, -d))
            if i==7:
                f.write('%f %f %f\n' % (x, -d/math.sqrt(2),-d/math.sqrt(2)))
            
        if c == "Stop\n":
            break
        x+=200.0;
        cnt+=1;
        print(cnt)
        
            
    f.close()
    print("Closing: " + s.name)
    s.close()
        

    
    print("Testing I- for point cloud ...")
    pcd = o3d.io.read_point_cloud("demofile.xyz", format = 'xyz')
    
    print(pcd)
    
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd])

    pt1=0
    pt2=1
    pt3=2
    pt4=3
    pt5=4
    pt6=5
    pt7=6
    pt8=7
    po=0

    lines = []

    for x in range(cnt):
        lines.append([pt1+po,pt2+po])
        lines.append([pt2+po,pt3+po])
        lines.append([pt3+po,pt4+po])
        lines.append([pt4+po,pt5+po])
        lines.append([pt5+po,pt6+po])
        lines.append([pt6+po,pt7+po])
        lines.append([pt7+po,pt8+po])
        lines.append([pt8+po,pt1+po])
        po += 8;

    pt1=0
    pt2=1
    pt3=2
    pt4=3
    pt5=4
    pt6=5
    pt7=6
    pt8=7
    po = 0
    do = 8

    for x in range(cnt-1):
        lines.append([pt1+po,pt1+do+po])
        lines.append([pt2+po,pt2+do+po])
        lines.append([pt3+po,pt3+do+po])
        lines.append([pt4+po,pt4+do+po])
        lines.append([pt5+po,pt5+do+po])
        lines.append([pt6+po,pt6+do+po])
        lines.append([pt7+po,pt7+do+po])
        lines.append([pt8+po,pt8+do+po])
        po+=8;
        
    line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)), lines=o3d.utility.Vector2iVector(lines))

    o3d.visualization.draw_geometries([line_set])












        



    
    
