"""
Exercise 4: Debugging train_gan function

BUGS:
1. STRUCTURAL: batch_size parameter hardcoded when creating labels, but actual batch
   from DataLoader might be smaller (especially last batch). Causes dimension mismatch.
2. COSMETIC: Typo "Generater" instead of "Generator" in docstring

FIX:
1. Use actual_batch_size = real_samples.size(0) instead of batch_size parameter
2. Fix typo in docstring
"""

import csv
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time


class Generator(nn.Module):
    """Generator class for the GAN"""
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 784),
            nn.Tanh(),
        )

    def forward(self, x):
        output = self.model(x)
        output = output.view(x.size(0), 1, 28, 28)
        return output


class Discriminator(nn.Module):
    """Discriminator class for the GAN"""
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(784, 1024),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = x.view(x.size(0), 784)
        output = self.model(x)
        return output


def train_gan_buggy(batch_size: int = 32, num_epochs: int = 2, device: str = "cpu"):
    """
    BUGGY VERSION - Uses hardcoded batch_size instead of actual batch size
    """
    print("=" * 60)
    print("EXERCISE 4: Debugging train_gan Function (BUGGY VERSION)")
    print("=" * 60)
    print(f"\nTraining GAN with batch_size={batch_size}, num_epochs={num_epochs}")
    print("⚠️  This version will fail when batch_size doesn't divide dataset evenly!")
    
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    
    try:
        train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
    except:
        print("Failed to download MNIST, retrying with different URL")
        torchvision.datasets.MNIST.resources = [
            ('https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz',
             'f68b3c2dcbeaaa9fbdd348bbdeb94873'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz',
             'd53e105ee54ea40749a09fcbcd1e9432'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz',
             '9fb629c4189551a2d022fa330f9573f3'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz',
             'ec29112dd5afa0611ce80d1b7f02629c')
        ]
        train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
    
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
    
    # Set up training
    discriminator = Discriminator().to(device)
    generator = Generator().to(device)
    lr = 0.0001
    loss_function = nn.BCELoss()
    optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
    optimizer_generator = torch.optim.Adam(generator.parameters(), lr=lr)
    
    # train
    for epoch in range(num_epochs):
        for n, (real_samples, mnist_labels) in enumerate(train_loader):
            try:
                # Data for training the discriminator
                real_samples = real_samples.to(device=device)
                # BUG: Uses hardcoded batch_size instead of actual batch size
                real_samples_labels = torch.ones((batch_size, 1)).to(device=device)
                latent_space_samples = torch.randn((batch_size, 100)).to(device=device)
                generated_samples = generator(latent_space_samples)
                generated_samples_labels = torch.zeros((batch_size, 1)).to(device=device)
                all_samples = torch.cat((real_samples, generated_samples))
                all_samples_labels = torch.cat((real_samples_labels, generated_samples_labels))
                
                # Training the discriminator
                discriminator.zero_grad()
                output_discriminator = discriminator(all_samples)
                loss_discriminator = loss_function(output_discriminator, all_samples_labels)
                loss_discriminator.backward()
                optimizer_discriminator.step()
                
                # Data for training the generator
                latent_space_samples = torch.randn((batch_size, 100)).to(device=device)
                
                # Training the generator
                generator.zero_grad()
                generated_samples = generator(latent_space_samples)
                output_discriminator_generated = discriminator(generated_samples)
                loss_generator = loss_function(output_discriminator_generated, real_samples_labels)
                loss_generator.backward()
                optimizer_generator.step()
                
                if n % 100 == 0:
                    print(f"Epoch {epoch}, Batch {n}: D_loss={loss_discriminator.item():.4f}, G_loss={loss_generator.item():.4f}")
                    
            except RuntimeError as e:
                print(f"\n❌ ERROR at epoch {epoch}, batch {n}:")
                print(f"   {e}")
                print(f"   This happens because batch_size={batch_size} doesn't match actual batch size!")
                return


def train_gan_fixed(batch_size: int = 32, num_epochs: int = 2, device: str = "cpu"):
    """
    FIXED VERSION - Uses actual batch size from DataLoader
    """
    print("=" * 60)
    print("EXERCISE 4: Debugging train_gan Function (FIXED VERSION)")
    print("=" * 60)
    print(f"\nTraining GAN with batch_size={batch_size}, num_epochs={num_epochs}")
    print("✓ This version handles variable batch sizes correctly!")
    
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    
    try:
        train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
    except:
        print("Failed to download MNIST, retrying with different URL")
        torchvision.datasets.MNIST.resources = [
            ('https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz',
             'f68b3c2dcbeaaa9fbdd348bbdeb94873'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz',
             'd53e105ee54ea40749a09fcbcd1e9432'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz',
             '9fb629c4189551a2d022fa330f9573f3'),
            ('https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz',
             'ec29112dd5afa0611ce80d1b7f02629c')
        ]
        train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
    
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
    
    # Set up training
    discriminator = Discriminator().to(device)
    generator = Generator().to(device)
    lr = 0.0001
    loss_function = nn.BCELoss()
    optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
    optimizer_generator = torch.optim.Adam(generator.parameters(), lr=lr)
    
    # train
    for epoch in range(num_epochs):
        for n, (real_samples, mnist_labels) in enumerate(train_loader):
            # Data for training the discriminator
            real_samples = real_samples.to(device=device)
            # FIX: Use actual batch size instead of hardcoded batch_size parameter
            actual_batch_size = real_samples.size(0)
            real_samples_labels = torch.ones((actual_batch_size, 1)).to(device=device)
            latent_space_samples = torch.randn((actual_batch_size, 100)).to(device=device)
            generated_samples = generator(latent_space_samples)
            generated_samples_labels = torch.zeros((actual_batch_size, 1)).to(device=device)
            all_samples = torch.cat((real_samples, generated_samples))
            all_samples_labels = torch.cat((real_samples_labels, generated_samples_labels))
            
            # Training the discriminator
            discriminator.zero_grad()
            output_discriminator = discriminator(all_samples)
            loss_discriminator = loss_function(output_discriminator, all_samples_labels)
            loss_discriminator.backward()
            optimizer_discriminator.step()
            
            # Data for training the generator
            latent_space_samples = torch.randn((actual_batch_size, 100)).to(device=device)
            
            # Training the generator
            generator.zero_grad()
            generated_samples = generator(latent_space_samples)
            output_discriminator_generated = discriminator(generated_samples)
            loss_generator = loss_function(output_discriminator_generated, real_samples_labels)
            loss_generator.backward()
            optimizer_generator.step()
            
            if n % 100 == 0:
                print(f"Epoch {epoch}, Batch {n}: D_loss={loss_discriminator.item():.4f}, G_loss={loss_generator.item():.4f}")
    
    print("\n✓ Training completed successfully!")


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 4: Debugging train_gan Function")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("ISSUES IN BUGGY VERSION:")
    print("  1. STRUCTURAL: Uses hardcoded batch_size instead of actual batch size")
    print("  2. COSMETIC: Typo 'Generater' instead of 'Generator'")
    print("=" * 60)
    
    print("\nNote: This exercise requires PyTorch and will download MNIST dataset.")
    print("      For demonstration, we'll use a small number of epochs.")
    
    # Test with batch_size=64 which triggers the bug
    print("\n1. Testing BUGGY version with batch_size=64:")
    print("   (This will fail on the last batch)")
    try:
        train_gan_buggy(batch_size=64, num_epochs=1, device="cpu")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    input("\nPress Enter to continue to fixed version...")
    
    print("\n2. Testing FIXED version with batch_size=64:")
    print("   (This will work correctly)")
    train_gan_fixed(batch_size=64, num_epochs=1, device="cpu")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("  Bug 1: Hardcoded batch_size causes dimension mismatch")
    print("  Bug 2: Typo in docstring")
    print("  Fix: Use actual_batch_size = real_samples.size(0)")
    print("=" * 60)

