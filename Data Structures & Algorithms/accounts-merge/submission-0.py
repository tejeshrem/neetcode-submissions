class UnionFind:
    
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x:int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a:int, b:int):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
      
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        union_find = UnionFind(len(accounts))
        email_to_account_index = {}

        for account_index, account_data in enumerate(accounts):
            name = account_data[0]
            emails = account_data[1:]
        
            for email in emails:
                if email in email_to_account_index:
                    existing_account_index = email_to_account_index[email]
                    union_find.union(account_index, existing_account_index)
                else:
                    email_to_account_index[email] = account_index

        root_to_emails = defaultdict(set)

        for account_index, account_data in enumerate(accounts):
            name = account_data[0]
            emails = account_data[1:]

            root_index = root_index = union_find.find(account_index)
            root_to_emails[root_index].update(emails)

        result = []
        for root_index, email_set in root_to_emails.items():
            account_name = accounts[root_index][0]
            merged_account = [account_name] + sorted(email_set)
            result.append(merged_account)
        return result



        