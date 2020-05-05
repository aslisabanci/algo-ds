def move(height, src, dest, over):
    if height >= 1:
        move(height - 1, src, over, dest)
        print(f"moving disk from {src} to {dest}")
        move(height - 1, over, dest, src)


move(3, "a", "b", "c")
