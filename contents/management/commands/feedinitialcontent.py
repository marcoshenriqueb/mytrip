from django.core.management.base import BaseCommand, CommandError
from contents.models import Content, Page

class Command(BaseCommand):
    help = 'Feeds initial indexes and texts for site content'

    def handle(self, *args, **options):
        home = Page(name='Home', user_id=1)
        home.save()

        c = Content(key='Titulo', page=home, text='Soluções Com Drones', user_id=1)
        c.save()

        c = Content(key='Subtitulo', page=home, text='Lorem ipsum dolor sit amet, consectetur adipisicing elit.', user_id=1)
        c.save()

        c = Content(key='Titulo quem somos', page=home, text='Quem somos', user_id=1)
        c.save()

        c = Content(key='Subtitulo quem somos', page=home, text='Uma breve descrição', user_id=1)
        c.save()

        c = Content(key='Texto quem somos', page=home, text='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam debitis voluptatem porro ut quod hic dolorem ullam aliquam accusamus, beatae quam deleniti quidem minima exercitationem. Cum rerum id, accusamus ea! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Enim distinctio, sequi officia quibusdam a accusantium rerum quis vel ad fuga. Earum itaque deleniti doloribus veniam accusamus aliquid corrupti provident adipisci.', user_id=1)
        c.save()

        c = Content(key='Titulo servicos', page=home, text='Nossos Serviços', user_id=1)
        c.save()
        
        c = Content(key='Titulo projetos', page=home, text='Projetos Recentes', user_id=1)
        c.save()

        c = Content(key='Titulo depoimentos', page=home, text='Nossos Clientes', user_id=1)
        c.save()

        c = Content(key='Titulo contato', page=home, text='Contato', user_id=1)
        c.save()

        c = Content(key='Texto contato', page=home, text='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Similique nobis aspernatur accusamus cum repellendus inventore cupiditate adipisci dolor, fugiat nemo necessitatibus ducimus! Fugit dolorem atque nemo quisquam veritatis modi excepturi?', user_id=1)
        c.save()

        c = Content(key='Endereco contato', page=home, text='Av das Américas 8888, Rio de Janeiro, Brasil', user_id=1)
        c.save()

        c = Content(key='Numero e email', page=home, text='(102) 3456 789 / info@thememove.com', user_id=1)
        c.save()