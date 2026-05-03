from collections import Counter

class TopicExtractor:
    def extract(self, posts, max_topics=5):
        all_topics = []
        for post in posts:
            if post.get('topics'):
                all_topics.extend([t.strip() for t in post['topics'].split(',')])
        
        counts = Counter(all_topics)
        return counts.most_common(max_topics)
