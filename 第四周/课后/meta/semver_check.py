from packaging.specifiers import SpecifierSet

versions = ["1.2.9", "1.3.0", "1.3.8", "1.9.0", "2.0.0"]

for rule in ["~=1.3", "==1.3.*", ">=1.3,<2"]:
    matched = [v for v in versions if v in SpecifierSet(rule)]
    print(f"{rule:10} -> {matched}")