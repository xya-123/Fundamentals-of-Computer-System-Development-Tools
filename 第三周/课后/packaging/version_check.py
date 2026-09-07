from packaging.specifiers import SpecifierSet

versions = ["1.9.0", "2.0.0", "2.1.5", "2.9.0", "3.0.0"]
rules = [">=2.0", ">=2.0,<3.0", "~=2.1.0"]

for rule in rules:
    allowed = SpecifierSet(rule)
    matched = [v for v in versions if v in allowed]
    print(f"{rule:12} -> {matched}")