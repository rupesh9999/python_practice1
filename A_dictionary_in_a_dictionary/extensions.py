extensions = {
    'python': '.py',
    'javascript': '.js',
    'java': '.java',
    'c++': '.cpp',
    'c': '.c',
    'html': '.html',
    'css': '.css',
    'php': '.php',
    'ruby': '.rb',
    'swift': '.swift',
}

for language, extension in extensions.items():
    print(f"The extension for {language.title()} is {extension}")
