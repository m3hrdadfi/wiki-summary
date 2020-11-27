from datasets import load_dataset

cache_dir = None

# Version 2.0.0
train_set = load_dataset('./wiki_summary_persian', '2.0.0', split='train', cache_dir=cache_dir)
dev_set = load_dataset('./wiki_summary_persian', '2.0.0', split='validation', cache_dir=cache_dir)
test_set = load_dataset('./wiki_summary_persian', '2.0.0', split='test', cache_dir=cache_dir)

print('VERSION 2.0.0')
print(f'train_set \n {train_set}')
print(f'dev_set \n {dev_set}')
print(f'test_set \n {test_set}')
print()
print()

# Version 1.0.0
train_set = load_dataset('./wiki_summary_persian', '1.0.0', split='train', cache_dir=cache_dir)
dev_set = load_dataset('./wiki_summary_persian', '1.0.0', split='validation', cache_dir=cache_dir)
test_set = load_dataset('./wiki_summary_persian', '1.0.0', split='test', cache_dir=cache_dir)

print('VERSION 1.0.0')
print(f'train_set \n {train_set}')
print(f'dev_set \n {dev_set}')
print(f'test_set \n {test_set}')
print()
print()
