class Solution:
    def invertImg(self, img: List[int]) -> List[int]:
        for i in range(len(img)):
            if(img[i] == 1):
                img[i] = 0
            else:
                img[i] = 1
        return img
    
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            temp = image[i][::-1]
            image[i] = self.invertImg(temp)
        return image
            
    
            
        