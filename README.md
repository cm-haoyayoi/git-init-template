# git-init-template for Python simple script

書き捨てるつもりだったPythonスクリプトを後から管理する用途目的のテンプレートです。
git initでtemplateに引数として渡すためのリソースではありません。

## HowTo
```
% wget -qO- -O tmp.zip https://codeload.github.com/cm-haoyayoi/python-git-manage-template/zip/master \
 && unzip tmp.zip \
 && rm tmp.zip \
 && mv python-git-manage-template-master/* . \
 && mv python-git-manage-template-master/.* . \
 && rm -rf python-git-manage-template-master
```

## virtualenv
```
% pipenv install --dev
% pipenv shell
```

## Test
```
% tox
```

