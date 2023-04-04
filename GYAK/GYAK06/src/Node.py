class Node():
    def __init__(self,feature_index=None,treshold=None,left=None,right=None,info_gain=None,value=None):
        #leaf
        self.value=value

        #dis
        self.feature_index=feature_index
        self.treshold=treshold
        self.left=left
        self.right=right
        self.info_gain=info_gain