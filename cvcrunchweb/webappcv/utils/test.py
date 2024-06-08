import torch
import time

size = 5000
a = torch.rand(size, size).cuda()
b = torch.rand(size, size).cuda()

start_time = time.time()
c = torch.matmul(a, b)
torch.cuda.synchronize()  # Wait for the GPU to finish before stopping the timer
end_time = time.time()
print(torch.__version__)
print(torch.cuda.is_available())

print(f"GPU computation time: {end_time - start_time} seconds")

