"""
Management command to seed EventNest with realistic demo data.
Creates categories, services, and store products for development/demo purposes.
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import ServiceCategory, Service, StoreCategory, StoreItem


class Command(BaseCommand):
    help = 'Seeds the database with realistic demo services and products'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting EventNest demo data seeding...'))

        try:
            with transaction.atomic():
                # Create categories and items
                self._create_service_categories()
                self._create_services()
                self._create_store_categories()
                self._create_store_items()

                self.stdout.write(self.style.SUCCESS('\n✓ Demo data seeded successfully!'))
                self.stdout.write(self.style.SUCCESS('  - Service categories created'))
                self.stdout.write(self.style.SUCCESS('  - 8 services created'))
                self.stdout.write(self.style.SUCCESS('  - Store categories created'))
                self.stdout.write(self.style.SUCCESS('  - 8 products created'))
                self.stdout.write(self.style.SUCCESS('\nYou can now visit /services/ and /store/ to see the data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n✗ Error seeding data: {str(e)}'))
            raise

    def _create_service_categories(self):
        """Create service categories"""
        categories = [
            {'name': 'Event Planning', 'description': 'Professional event planning and management services'},
            {'name': 'Photography', 'description': 'Professional photography and videography services'},
            {'name': 'Catering', 'description': 'Food and beverage catering services'},
            {'name': 'Decoration', 'description': 'Event decoration and setup services'},
            {'name': 'Printing', 'description': 'Printing services for invitations and materials'},
            {'name': 'Entertainment', 'description': 'DJ, music, and entertainment services'},
        ]

        for cat_data in categories:
            category, created = ServiceCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'  → Created service category: {category.name}')

    def _create_services(self):
        """Create demo services"""
        services_data = [
            {
                'category_name': 'Event Planning',
                'title': 'Wedding Event Management',
                'description': 'Complete wedding planning service including venue selection, vendor coordination, guest management, and day-of coordination. Our experienced team will handle every detail of your special day, from the initial consultation to the final send-off. We work with the best venues and vendors in Bangladesh to ensure your wedding is perfect.',
                'price': 25000,
            },
            {
                'category_name': 'Event Planning',
                'title': 'Corporate Event Planning',
                'description': 'Professional corporate event planning for conferences, seminars, product launches, and team building activities. We handle venue booking, AV equipment, catering, registration, and all logistics. Perfect for businesses looking to make a lasting impression on clients and employees.',
                'price': 35000,
            },
            {
                'category_name': 'Event Planning',
                'title': 'Birthday Party Planning',
                'description': 'Creative and fun birthday party planning for all ages. We offer themed parties for kids and elegant celebrations for adults. Services include venue decoration, entertainment booking, catering coordination, and party favors. Make your birthday unforgettable with our expert planning.',
                'price': 12000,
            },
            {
                'category_name': 'Photography',
                'title': 'Professional Photography',
                'description': 'High-quality event photography with professional editing and retouching. Package includes 6 hours of coverage, 200+ edited high-resolution photos, and online gallery. Delivery within 7 days. We specialize in weddings, corporate events, and family celebrations.',
                'price': 8000,
            },
            {
                'category_name': 'Catering',
                'title': 'Catering Service',
                'description': 'Delicious Bangladeshi and international cuisine prepared by experienced chefs. Our catering service includes menu planning, food preparation, serving staff, and cleanup. We offer vegetarian, non-vegetarian, and custom menu options. Minimum 50 guests. Perfect for weddings, corporate events, and parties.',
                'price': 15000,
            },
            {
                'category_name': 'Decoration',
                'title': 'Decoration & Lighting',
                'description': 'Professional event decoration with ambient lighting, floral arrangements, and custom stage setup. Our design team will transform your venue into a stunning space. Services include theme decoration, lighting design, stage backdrop, entrance arch, and table centerpieces.',
                'price': 10000,
            },
            {
                'category_name': 'Printing',
                'title': 'Printing Services',
                'description': 'Custom printing services for invitation cards, banners, flyers, and event materials. We use premium paper and high-quality printing technology. Fast turnaround time. Services include design consultation, printing, and delivery. Perfect for weddings, corporate events, and special occasions.',
                'price': 600,
            },
            {
                'category_name': 'Entertainment',
                'title': 'Entertainment / DJ Service',
                'description': 'Professional DJ and entertainment services with premium sound system and lighting. Our experienced DJs know how to read the crowd and keep the party going. Services include music selection, MC services, special effects, and custom playlists. Perfect for weddings, parties, and corporate events.',
                'price': 5000,
            },
        ]

        for service_data in services_data:
            category = ServiceCategory.objects.get(name=service_data['category_name'])
            service, created = Service.objects.update_or_create(
                title=service_data['title'],
                defaults={
                    'category': category,
                    'description': service_data['description'],
                    'price': service_data['price'],
                    'image': '',  # Leave blank - will show placeholder
                }
            )
            if created:
                self.stdout.write(f'  → Created service: {service.title}')
            else:
                self.stdout.write(f'  → Updated service: {service.title}')

    def _create_store_categories(self):
        """Create store categories"""
        categories = [
            {'name': 'Decorations', 'description': 'Event decoration items and supplies'},
            {'name': 'Lighting', 'description': 'Lighting equipment and accessories'},
            {'name': 'Printing', 'description': 'Printed materials and stationery'},
            {'name': 'Party Packages', 'description': 'Complete party packages and bundles'},
        ]

        for cat_data in categories:
            category, created = StoreCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'  → Created store category: {category.name}')

    def _create_store_items(self):
        """Create demo store products"""
        products_data = [
            {
                'category_name': 'Decorations',
                'name': 'Balloon Decoration Kit',
                'description': 'Premium balloon decoration kit with 100+ colorful balloons in assorted colors, ribbons, balloon pump, and decorating strips. Perfect for birthday parties, weddings, and special events. Includes instruction guide for creating balloon arches and garlands.',
                'price': 1250,
                'stock': 50,
            },
            {
                'category_name': 'Lighting',
                'name': 'LED Fairy String Lights',
                'description': 'Beautiful 10-meter LED fairy string lights with 100 LED bulbs. Features 8 different lighting modes including steady on, twinkle, and wave. Available in warm white and multicolor. Battery and USB powered options. Waterproof for indoor and outdoor use.',
                'price': 850,
                'stock': 75,
            },
            {
                'category_name': 'Decorations',
                'name': 'Artificial Flower Bouquet',
                'description': 'Realistic artificial silk flower bouquet in vibrant colors. Features roses, lilies, and seasonal blooms arranged professionally. Perfect for table centerpieces, wedding decoration, and home decor. Reusable and requires no maintenance. Includes decorative vase.',
                'price': 950,
                'stock': 40,
            },
            {
                'category_name': 'Decorations',
                'name': 'Table Centerpiece Stand',
                'description': 'Elegant gold-plated metal table centerpiece stand for flowers, candles, and decoration items. Adjustable height from 40cm to 60cm. Sturdy base with intricate scroll design. Perfect for weddings and formal events. Set of 4 pieces.',
                'price': 1850,
                'stock': 25,
            },
            {
                'category_name': 'Printing',
                'name': 'Invitation Card Pack (50 pcs)',
                'description': 'Premium invitation card pack with 50 cards and envelopes. High-quality cardstock with elegant border designs. Blank inside for custom messages. Available in multiple colors and designs. Perfect for weddings, birthdays, and special occasions.',
                'price': 450,
                'stock': 100,
            },
            {
                'category_name': 'Decorations',
                'name': 'Event Welcome Board',
                'description': 'Wooden welcome board with black chalk surface and decorative wooden frame. Includes sturdy easel stand and 5 chalk markers in assorted colors. Size: 60cm x 90cm. Perfect for weddings, parties, and events. Reusable and easy to clean.',
                'price': 750,
                'stock': 30,
            },
            {
                'category_name': 'Party Packages',
                'name': 'Birthday Party Package',
                'description': 'Complete birthday party package for 20 guests. Includes colorful balloons, happy birthday banner, party hats, themed plates and cups, napkins, cutlery, and party favor bags. Available in multiple themes. Everything you need for an amazing birthday celebration.',
                'price': 2500,
                'stock': 20,
            },
            {
                'category_name': 'Party Packages',
                'name': 'Wedding Decor Package',
                'description': 'Premium wedding decoration bundle covering setup for 100 guests. Includes artificial flowers, string lights, table centerpieces, fabric draping, entrance arch decoration, and stage backdrop materials. Professional quality items perfect for creating an elegant wedding atmosphere.',
                'price': 5500,
                'stock': 10,
            },
        ]

        for product_data in products_data:
            category = StoreCategory.objects.get(name=product_data['category_name'])
            product, created = StoreItem.objects.update_or_create(
                name=product_data['name'],
                defaults={
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'image': '',  # Leave blank - will show placeholder
                }
            )
            if created:
                self.stdout.write(f'  → Created product: {product.name}')
            else:
                self.stdout.write(f'  → Updated product: {product.name}')
