INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(0,'Poppy Seeds','Small seeds that are a great topping ',1.99,0,'static/images/poppy_seeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(1,'Apples','An edible cultivation of the Malus genus.',2,100,'static/images/apple.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(2,'Bananas','A long curved fruit which grows in clusters and has soft pulpy flesh and yellow skin when ripe.',1,93,'static/images/banana.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(3,'Mangos','The best fruit on the planet.',4,100,'static/images/mango.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(4,'Watermelon','Large green oval-shaped fruit with a soft red inside.',10,100,'static/images/watermelon.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(5,'Pineapples','A tropical spiked fruit with a sour and sweet taste.',5,100,'static/images/pineapple.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(6,'Oranges','An orange sphere-shaped fruit.',2,100,'static/images/orange.jpeg','Fruit');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(7,'Bell Pepper','Red sweet pepper that is crunchy and adds color',0.79,100,'static/images/bell_peppers.jpeg','Vegetable');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(8,'Broccoli','Green flowering vegetable',1.49,100,'static/images/broccoli.jpeg','Vegetable');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(9,'Butter','Fatty substance that can be used as spread or in cooking',4.29,88,'static/images/butter.jpeg','Vegetable');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(10,'Carrots','Orange long root vegetable',0.99,96,'static/images/carrots.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(11,'Cheddar Cheese','Cheese with a sharp flavor and yellow color',7,100,'static/images/cheddar_cheese.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(12,'Chia Seeds','Small oval seeds that over many benefits',12,78,'static/images/chia_seeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(13,'Cucumber','Long green veggie that is crunchy',1.19,97,'static/images/cucumbers.jpeg','Vegetable');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(14,'Flax Seeds','Small seeds that over omega-3''s and other benefits',10.99,45,'static/images/flaxseeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(15,'Free Range Eggs','Chicken eggs from chickens that were free to roam',5.99,95,'static/images/free_range_eggs.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(16,'Greek Yogurt','High protien yogurt with no flavor added',7.99,55,'static/images/greek_yogurt.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(17,'Heavy Cream','Thick cream that can be used as an ingredient',3.79,89,'static/images/heavy_cream.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(18,'Milk','Whole milk from cows',3.29,100,'static/images/milk.jpeg','Dairy');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(19,'Pumpkin Seeds','Seeds from a pumpkin that can be used in many ways',3.69,100,'static/images/pumpkin_seeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(20,'Seasame Seeds','Small seeds that offer crunch and great to top dishes',4.49,67,'static/images/sesame_seeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(21,'Spinach','Green leafy veggie that is high in iron and great for salads',4.89,100,'static/images/Spinach.jpeg','Vegetable');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(22,'Sunflower Seeds','Roasted sunflower seeds with no flavor',1.89,100,'static/images/sunflower_seeds.jpeg','Seeds');
INSERT into `inventory` (`id`,`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES(23,'Tomatoes','Red veggie that gives a lot of flavors and color to dishes',1.69,99,'static/images/tomatoes.jpeg','Vegetable');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
