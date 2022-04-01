create user 'martina1'@'localhost' identified by 'password';

grant select on shopping_cart.* to 'martina1'@'localhost';

grant insert on shopping_cart.* to 'martina1'@'localhost';

revoke insert on shopping_cart.* from 'martina1'@'localhost';
