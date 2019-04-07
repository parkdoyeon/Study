//
//  BinaryTrees.h
//  DS08_BinaryTree
//
//  Created by Doyeon on 2018. 4. 15..
//  Copyright © 2018년 Doyeon. All rights reserved.
//

#ifndef BinaryTrees_h
#define BinaryTrees_h

#include <stdio.h>


typedef int BTData;

typedef struct _bTreeNode
{
    BTData data;
    struct _bTreeNode * left;
    struct _bTreeNode * right;
} BTreeNode;

BTreeNode * MakeBTreeNode(void);
BTData GetData(BTreeNode * bt);
void SetData(BTreeNode * bt, BTData data);

BTreeNode * GetLeftSubTree(BTreeNode * bt);
BTreeNode * GetRightSubTree(BTreeNode * bt);

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub);
void MakeRightSubTree(BTreeNode * main, BTreeNode * sub);

typedef void VisitFuncPtr(BTData data);

void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action);
void InorderTraverse(BTreeNode* bt, VisitFuncPtr action);
void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action);


#endif /* BinaryTrees_h */
