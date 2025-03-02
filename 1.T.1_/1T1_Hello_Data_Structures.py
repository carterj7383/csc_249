class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Let's create a queue and demonstrate it in action
if __name__ == "__main__":
    print("The BS-Hit Duo to the rescue! Creating a queue to stop Mr. Norris...\n")

    # Initialize the queue
    queue = Queue()

    # Add some elements to the queue (enqueue)
    print("Enqueueing tasks to stop Mr. Norris:")
    tasks = ["Disable CI/CD traps", "Locate Mr. Norris", "Deploy anti-Norris shield", "Save the day"]
    for task in tasks:
        queue.enqueue(task)
        print(f"Added to queue: {task}")

    print(f"\nCurrent queue: {queue}\n")

    # Process the queue (dequeue)
    print("Processing the queue to complete tasks:")
    while not queue.is_empty():
        current_task = queue.dequeue()
        print(f"Processing task: {current_task}")
        print(f"Remaining queue: {queue}\n")

    print("All tasks completed! Mr. Norris has been neutralized. The BS-Hit duo have once again saved the day again! ")