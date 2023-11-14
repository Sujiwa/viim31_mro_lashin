import random
import numpy as np
import matplotlib.pyplot as plt

class HorizontalStripesGenerator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.num_classes = 0
        self.dimension = 0
        self.class_sizes = []

    def read_input(self):
        with open(self.input_file, 'r') as file:
            self.num_classes = int(file.readline())
            self.dimension = int(file.readline())
            self.class_sizes = [random.randint(1, 7) for _ in range(self.dimension)]

    def generate_data(self):
        all_classes_data = []
        for class_index in range(self.num_classes):
            class_patterns = []
            for _ in range(self.dimension):
                pattern = [1] * random.randint(1, self.class_sizes[class_index])
                pattern += [0] * (self.dimension - len(pattern))
                random.shuffle(pattern)
                class_patterns.append(pattern)
            all_classes_data.append(class_patterns)
        return all_classes_data

    def save_data(self, data, output_file):
        with open(output_file, 'w') as file:
            for i, class_data in enumerate(data):
                file.write(f"Class {i + 1}:\n")
                for pattern in class_data:
                    file.write(' '.join(map(str, pattern)) + '\n')
                file.write('\n')

    def display_data(self, data):
        for i, class_data in enumerate(data):
            print(f"Class {i + 1}:")
            for pattern in class_data:
                print(pattern)
            print()

    def visualize_data(self, data):
        colors = plt.cm.rainbow(np.linspace(0, 1, self.num_classes))

        fig, axs = plt.subplots(self.num_classes, 1, figsize=(8, 1.6 * self.num_classes))
        fig.suptitle("All Classes")

        plt.subplots_adjust(hspace=1)

        for i, class_data in enumerate(data):
            max_length = max(len(pattern) for pattern in class_data)
            filled_class_data = [pattern + [0] * (max_length - len(pattern)) for pattern in class_data]

            class_data_array = np.array(filled_class_data)
            axs[i].imshow(class_data_array, cmap='gray_r', interpolation='nearest', aspect='auto', alpha=0.7)
            axs[i].set_title(f"Class {i + 1}")
            axs[i].set_xlabel("Pattern Dimension")
            axs[i].set_ylabel("Samples")
            axs[i].axis('on')

        plt.show()

if __name__ == "__main__":
    generator = HorizontalStripesGenerator("input.txt")
    generator.read_input()
    generated_data = generator.generate_data()
    
    print("Generated Data:")
    generator.display_data(generated_data)

    output_file = "output.txt"
    generator.save_data(generated_data, output_file)
    print(f"Generated data saved to {output_file}")

    print("Visualizing Generated Data:")
    generator.visualize_data(generated_data)
