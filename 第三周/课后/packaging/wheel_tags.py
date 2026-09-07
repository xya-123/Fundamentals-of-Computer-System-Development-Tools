from packaging.tags import sys_tags
from packaging.utils import parse_wheel_filename

wheel = "greetlab_25060012033-0.1.0-py3-none-any.whl"
name, version, build, wheel_tags = parse_wheel_filename(wheel)
system_tags = set(sys_tags())

print("name:", name)
print("version:", version)
print("wheel tags:", ", ".join(map(str, wheel_tags)))
print("compatible:", bool(set(wheel_tags) & system_tags))
print("first system tags:")

for tag in list(sys_tags())[:5]:
    print(" ", tag)