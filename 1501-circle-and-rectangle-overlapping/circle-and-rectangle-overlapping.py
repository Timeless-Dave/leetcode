class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = min(max(xCenter, x1), x2)
        cy = min(max(yCenter, y1),y2)
        dx = cx - xCenter
        dy = cy - yCenter
        return dx*dx + dy*dy <= radius*radius