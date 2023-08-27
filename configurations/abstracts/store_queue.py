import queue

class StoreQueue:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreQueue, cls).__new__(cls)
            cls._instance.queue = queue.Queue()
            cls._instance.unique_items = set()
        return cls._instance

    def put(self, item, key="id"):
        value = item.get(key)
        self.queue.put(item)
        self.unique_items.add(value)

    def massive_put(self, items, key="id"):
        for i in items:
            value = i.get(key)
            if value is not None and value not in self.unique_items:
                self.queue.put(i)
                self.unique_items.add(value)

    def get(self, key="id"):
        if not self.queue.empty():
            item = self.queue.get()
            self.unique_items.remove(item.get(key))
            return item
        else:
            return None

    def get_all(self, key="id"):
        all_items = []
        while not self.queue.empty():
            item = self.queue.get()
            self.unique_items.remove(item.get(key))
            all_items.append(item)
        return all_items

    def size(self):
        return self.queue.qsize()
