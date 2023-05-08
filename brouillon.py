from LinguaPythonica.Laspak.Root import LaspakRoot
from LinguaPythonica.Laspak.Assembling import root_dictionnary

for root in LaspakRoot.dict_root.values():
    print(root,root.translation)