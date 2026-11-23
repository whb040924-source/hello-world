import argparse

parser = argparse.ArgumentParser(description="向指定的人打招呼")
parser.add_argument("name", help="对方的名字")
parser.add_argument("--upper", action="store_true", help="用大写输出")
args = parser.parse_args()

message = f"Hello, {args.name}!"
print(message.upper() if args.upper else message)
