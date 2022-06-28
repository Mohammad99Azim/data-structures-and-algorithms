class NodeAnimal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rare = None

    def __str__(self):
        loo = self.front
        print('\u2190 AnimalShelter \u2190 \n')
        print('\u2190   \u2190  \u2190')
        while loo:
            print("(" + str(loo.type) + " ," + str(loo.name) + ")", end="")
            loo = loo.next
        return "\n _______"

    def enqueue(self, animal):
        if self.front is None:
            self.front = animal
            self.rare = animal
        else:
            self.rare.next = animal
            self.rare = animal

    def dequeue(self, pref):
        if self.front is None:
            raise Exception("Can\'t dequeue The AnimalShelter is Empty")

        if pref != 'cat' and pref != 'dog':  # Start Stretch Goal
            if self.front.type != 'cat' and self.front.type != 'dog':
                self.front = self.front.next
                return pref
            temp = self.front
            sec = self.front.next
            while sec:
                if sec.type != 'cat' and sec.type != 'dog':
                    temp.next = sec.next
                    if sec.next is None:
                        self.rare = temp
                    return pref
                temp = temp.next
                sec = sec.next  # End Stretch Goal
            return None

        if self.front.type == pref:
            self.front = self.front.next
            return pref

        temp = self.front
        sec = self.front.next
        while sec:
            if sec.type == pref:
                temp.next = sec.next
                if sec.next is None:
                    self.rare = temp
                return pref
            temp = temp.next
            sec = sec.next


if __name__ == '__main__':
    dog1 = NodeAnimal("dog", "dogOne")
    dog2 = NodeAnimal("dog", "dog2")
    dog3 = NodeAnimal("dog", "dog3")
    cat1 = NodeAnimal("cat", "cat1")
    cat2 = NodeAnimal("cat", "cat2")
    cat3 = NodeAnimal("cat", "cat3")
    no_type1 = NodeAnimal("noType1", "noName1")
    no_type2 = NodeAnimal("noType2", "noName2")

    shelter = AnimalShelter()

    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    shelter.dequeue("cat")
    shelter.dequeue("dog")
    shelter.enqueue(no_type1)
    shelter.enqueue(no_type2)
    shelter.dequeue("noTy")
    shelter.dequeue("noTy")


    print(shelter)
    print(shelter.rare.name)

