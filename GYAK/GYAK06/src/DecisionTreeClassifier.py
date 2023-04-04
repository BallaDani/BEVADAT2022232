import numpy as np
from src.Node import Node

class DecisionTreeClassifier():
    def __init__(self,min_sample_split=2,max_depth=2) -> None:
        self.max_depth=max_depth
        self.min_sample_split=min_sample_split

        self.root=None
    def build_tree(self,dataset,curr_depth=0):
        X,Y=dataset[::-1],dataset[:,-1]

        num_sample,num_feature=np.shape(X)

        if  num_sample>=self.min_sample_split and curr_depth<=self.max_depth:
            best_split=self.get_best_split(dataset,num_sample,num_feature)

            if best_split['info_gain']>0:
                left_subtree=self.build_tree(best_split['dataset_left'],curr_depth+1)
                rigth_subtree=self.build_tree(best_split['dataset_rigth'],curr_depth+1)
                return Node(best_split['feature_index'],best_split['treshold'],left_subtree,rigth_subtree,best_split['info_gain'])
            
            



    def get_best_spli(self, dataset,num_sample,num_feature):
        best_split=()
        max_info_gain=float('inf')

        for feature_index in range(num_feature):
            feature_value=dataset[:,feature_index]
            possible_treshold=np.unique(feature_value)

            for treshold in possible_treshold:
                dataset_left,dataset_rigth,=self.split(dataset, feature_index, treshold)
                if len(dataset_left)>0 and len(dataset_rigth)>0:
                    y,left_y,rigth_y=dataset[:-1],dataset_left[:-1],dataset_rigth[:-1]

                    curr_info_gain=self.information_gain(y,left_y,rigth_y,'gini')

                    if curr_info_gain>max_info_gain:
                        best_split['feature_index']=feature_index
                        best_split['treshold']=treshold
                        best_split['dataset_left']=dataset_left
                        best_split['dataset_rigth']=dataset_rigth
                        best_split['info_gain']=curr_info_gain

                        max_info_gain=curr_info_gain

        return best_split
    


    def split(self,dataset,feature_index,treshold):
        dataset_left=np.array([row for row in dataset if row[feature_index]<=treshold])
        dataset_rigth=np.array([row for row in dataset if row[feature_index]>treshold])

        return dataset_left,dataset_rigth
    

    def information_gain(self,parent,l_child,r_child,mode='entropy'):
        weight_l=len(l_child)/len(parent)
        weight_r=len(l_child)/len(parent)


        gain=self.gini_index(parent)-(weight_l*self.gini_index(l_child)+weight_r*self.gini_index(r_child))

        return gain

    def gini_index(self,y):
        class_labels=np.unique(y)
        gini=0
        for cls in class_labels:
            p_cls=len(y[y==cls])/len(y)
            gini+=p_cls**2

        return 1-gini
    def calculate_leaf_node(self,y):
        y=list(y)
        return max(y,key=(y.count))

    def print_tree(self,tree=None,indent=" "):
        if not tree:
            tree=self.root

        if tree.value is not None:
            print(tree.value)
        else:
            print("x_"+str(tree.feature_index),"<=",tree.treshold,"?", tree.info_gain)
            print("%s left:" %(indent),end="")
            self.print_tree(tree.left,indent=indent)
            print("%s left:" %(indent),end="")     
            self.print_tree(tree.left,indent=indent)

    def fit(self,x,y):
        dataset=np.concatenate((x,y),axis=1)
        self.root=self.build_tree(dataset)

    def predict(self,X):
        prediciton=[self.make_prediction(x,self.root) for x in X]
        return prediciton

    def make_prediction(self,x,tree):
        if  tree.value!=None:
            return tree.value
        feature_val=x[tree.feature_index]
        if (feature_val<tree.treshold):
            return self.make_prediction(x,tree.left)
        else:
            return self.make_prediction(x, tree.rigth)



