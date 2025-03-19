
import os
import subprocess

def code_style_check():
    # リポジトリ内のすべてのPythonファイルをチェックする
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    # flake8を実行して、コードのスタイルをチェックする
                    result = subprocess.run(
                        ["flake8", filepath],
                        capture_output=True,
                        text=True,
                        check=True)
                    print(f"Style check for {filepath}: OK")
                    print(f"Return code: {result.returncode}")
                except subprocess.CalledProcessError as e:
                    print(f"Style check for {filepath}: FAILED")
                    print(e.output)


if __name__ == "__main__":
    code_style_check()
