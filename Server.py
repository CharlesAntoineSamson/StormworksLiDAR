from http.server import HTTPServer, BaseHTTPRequestHandler
import math
import numpy as np
import open3d as o3d
import datetime
#import atexit

now_raw = datetime.datetime.now()
now_2 = now_raw.strftime("%Y-%m-%d %H:%M:%S")
now_3 = now_2.replace(" ","")
now_4 = now_3.replace("'","")


def addToArray(point):
    if 'point_list' not in globals():
        global point_list
        point_list = []
    point_list.append(point)
    if 'np_xyz' or 'np_xyz_f' not in globals():
        global np_xyz
        global np_xyz_f
        np_xyz= np.array([],dtype=object)
        np_xyz_f= np.array([],dtype=object)
    np_xyz = np.array(point_list)
    dim = np_xyz.shape[0]+1
    np_xyz_f = np_xyz #np_xyz.reshape((dim,3))


def save():
    name = "Output_"+now_4
    #print(name)
    np_xyz_f.ravel()
    np.savetxt("Output.storm3d",np_xyz_f)
    print("file saved as "+name)
    print("--------------------")
    #print(np_xyz_f)
    #print("--------------------")
    print(np_xyz_f.shape)

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello World".encode())
        point_raw = self.path
        point = point_raw.replace("/","")
        if point == "stop":
            save()
        else:
            points = point.split("|")
            points_int = list(map(float, points))
            ##x,y,z
            x = points_int[0]*math.sin((points_int[2]+1)*90)
            y = math.sqrt((points_int[0]**2)-(x**2))
            z = points_int[1]
            xyz = [x,y,z]
            print(xyz)
            addToArray(xyz)

    def log_message(self, format, *args):
        return


#def render():
#    pcl = o3d.geometry.PointCloud()
#    pcl.points = o3d.utility.Vector3dVector(np_xyz)
#    o3d.visualization.draw_geometries([pcl])

#    numpy_points = np.asarray(pcl.points)
#    pcl.points = numpy_points

def main():
    PORT = 10000
    server = HTTPServer(("", PORT), helloHandler)
    print("Ready on Port", str(PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()



#atexit.register(save)
