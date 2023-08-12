# 知识产权案件知识图谱构建

- ### 数据源

​		在北大法宝和裁判文书网搜索与知识产权，尤其是著作权相关的判决书。最终抽取了108份判决书作为本项目的研究数据（保存在"data"文件夹中）。

- ### 数据处理

​		下载的判决书以txt文档呈现，大致可以分为几大部分：（1）当事人、委托人情况（2）原告请求（3）被告辩护（4）裁判结果（5）法院认定事实（6）法院认为（7）裁判结果。判决书陈述的过程中划分了较多的段落，段落之间用换行符隔开，通过换行符对判决书进行分割，一共得到22133条法律文本数据（保存在"判决书内容.xlsx"和"data_forlabel"文件夹中）。
​		利用doccano**[1]**工具对所得的文本进行标注。这里仅对实体及其属性值进行标注，因为法律知识图谱往往以 < 实体，属性，属性值 > 为主，以 < 实体，关系，实体 > 为辅，从而提炼并抽象法律的一般实践规范。**[2]**选取了其中的10份判决书的文本数据进行标注，具体标注各实体数量如下图所示：

![image-20230812181845852](C:\Users\tang\AppData\Roaming\Typora\typora-user-images\image-20230812181845852.png)



### 模型训练

​		利用doccano标注后的数据可直接利用Paddlenlp**[3]**自然语言处理库的UIE信息抽取统一框架进行训练。对标注数据按照8：1：1的比例划分训练集、验证集和测试集。训练的参数基本参照UIE文档"4.3模型微调"中的参数，模型训练结果保存在"./PaddleNLP-develop/model_zoo/uie/checkpoint"文件夹中。

### 模型评估

以F1值评价实体抽取结果，考虑到裁判结果、抗辩理由的实体长度较长，难以抽取，在测试集取得77.5%的F1值已能说明模型能有较好的抽取效果。
验证集结果：

![image-20230812182634877](C:\Users\tang\AppData\Roaming\Typora\typora-user-images\image-20230812182634877.png)

测试集结果：

![image-20230812182652406](C:\Users\tang\AppData\Roaming\Typora\typora-user-images\image-20230812182652406.png)

### 知识图谱绘制

抽取200个节点的结果：

<img src="C:\大数据实践+毕业论文\中政法比赛\结果\result200.png" alt="result200" style="zoom:80%;" />

抽取1000个节点的结果：

![result1000](C:\大数据实践+毕业论文\中政法比赛\结果\result1000.png)

### 引文

[1] @misc{doccano,
  title={{doccano}: Text Annotation Tool for Human},
  url={https://github.com/doccano/doccano},
  note={Software available from https://github.com/doccano/doccano},
  author={
    Hiroki Nakayama and
    Takahiro Kubo and
    Junya Kamura and
    Yasufumi Taniguchi and
    Xu Liang},
  year={2018},
}
[2] DENG Y, SHEN Y, YANG M, et al. Knowledge as a bridge: Improving cross-domain answer selection with external knowledge[C]//Proceedings of the 29th International Conference on Computational Linguistics（2022）
[3] @ misc{=paddlenlp,
    title={PaddleNLP: An Easy-to-use and High Performance NLP Library},
    author={PaddleNLP Contributors},
    howpublished = {\url{https://github.com/PaddlePaddle/PaddleNLP}},
    year={2021}
}
