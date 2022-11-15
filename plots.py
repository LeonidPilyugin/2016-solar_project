import math
import matplotlib.pyplot as plt

def read():
    """Reads data from stats.txt"""
    global vxs
    global vys
    global xs
    global ys
    global ts

    file = open("stats.txt")
    vxs = []
    vys = []
    xs = []
    ys = []
    ts = []

    for line in file:
        _line = line.split()
        if len(_line) < 1:
            continue
        elif len(_line) == 1:
            ts.append(float(line))
        elif _line[0] == "planet":
            xs.append(float(_line[4]))
            ys.append(float(_line[5]))
            vxs.append(float(_line[6]))
            vys.append(float(_line[7]))
            
    file.close()
    
def plot_vr(file = None):
    """Plots v(r)"""
    global vxs
    global vys
    global xs
    global ys
    global ts
    
    vs = list(map(lambda x: math.hypot(x[0], x[1]), zip(vxs, vys)))
    rs = list(map(lambda x: math.hypot(x[0], x[1]), zip(xs, ys)))
    
    plt.title("v(r)")
    plt.xlabel("r")
    plt.ylabel("v")
    plt.plot(rs, vs)
    
    if file is None:
        plt.show()
    else:
        plt.savefig(file)
    
    
def plot_vt(file = None):
    """Plots v(t)"""
    global vxs
    global vys
    global xs
    global ys
    global ts
    
    vs = list(map(lambda x: math.hypot(x[0], x[1]), zip(vxs, vys)))
    
    plt.title("v(t)")
    plt.xlabel("t")
    plt.ylabel("v")
    plt.plot(ts, vs)
    
    if file is None:
        plt.show()
    else:
        plt.savefig(file)
    
    
def plot_rt(file = None):
    """Plots r(t)"""
    global vxs
    global vys
    global xs
    global ys
    global ts
    
    rs = list(map(lambda x: math.hypot(x[0], x[1]), zip(xs, ys)))
    
    plt.title("r(t)")
    plt.xlabel("t")
    plt.ylabel("r")
    plt.plot(ts, rs)
    
    if file is None:
        plt.show()
    else:
        plt.savefig(file)
    
    
if __name__ == "__main__":
    read()
    plot_rt("rt.png")
    plot_vt("vt.png")
    plot_vr("vr.png")

