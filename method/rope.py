import torch

x=torch.tensor([1.0,2.0,3.0,4.0])
y=torch.tensor([5.0,6.0,7.0,8.0])

#对 x 中每个元素判断是否大于 3，得到布尔张量
condition=x>3
print(condition)

result=torch.where(condition,x,y)
'''
如果 condition 对应位置为 True，取 x 中对应位置的值；

如果 condition 对应位置为 False，取 y 中对应位置的值。
'''
print(result)

#外积 aij=bi*cj
result2=torch.outer(x,y)
print(result2)

#拼接张量
t1 = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[13, 14, 15], [16, 17, 18]]])
t2 = torch.tensor([[[7, 8, 9], [10, 11, 12]], [[19, 20, 21], [22, 23, 24]]])
#按哪个维，哪个维就变
result3 = torch.cat((t1, t2), dim=0)
print(result3)

t1=torch.Tensor([1,2,3])
t2=t1.unsqueeze(0)
print(t1.shape)
print(t2)
print(t2.shape)
