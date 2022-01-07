import time


def cloudshow(self):
    """
    doc: 在窗口中新建一个点云显示组件
    :param self: 窗口类的self
    """
    #from util.vision.cloud_process import cloudshow
    #cloudshow(self)

    import numpy as np
    import pyqtgraph.opengl as gl
    from pyqtgraph.opengl import GLViewWidget
    self.graphicsView = GLViewWidget(self)
    # 显示坐标轴
    x = gl.GLLinePlotItem(pos=np.asarray([[0, 0, 0], [0.2, 0, 0]]), color=(1, 0, 0, 1), width=0.005)
    y = gl.GLLinePlotItem(pos=np.asarray([[0, 0, 0], [0, 0.2, 0]]), color=(0, 1, 0, 1), width=0.005)
    z = gl.GLLinePlotItem(pos=np.asarray([[0, 0, 0], [0, 0, 0.2]]), color=(0, 0, 1, 1), width=0.005)
    # 显示地板网格
    g = gl.GLGridItem()
    self.graphicsView.addItem(x)
    self.graphicsView.addItem(y)
    self.graphicsView.addItem(z)
    self.graphicsView.addItem(g)
    self.gridLayout_4.addWidget(self.graphicsView)
