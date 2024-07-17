# InformData | Automation Team | Python Web-Scraping Asssesment

### Task:
Using the `Python3` programming language with the `Microsoft Playwright` library, create a headless web-scraper that can navigate to the Amazon Daily Deals (located at https://www.amazon.com/deals).  The top of this page will contain a section of "Member-Only Prime Deals".  Your scraper should be able to grab all of the Prime Deals in the side-scrolling section at the top of this page and return a `list` of `dictionary` objects containing the following keys and their string values:
- `product-link` : a link to this product on Amazon's website
- `product-name` : the listed name of the product
- `list-price` : the original price for this item
- `discounted-price`: the "deal" price for this item

*NOTE:  You will need to create a branch off of this repository, and then once completed, push the changes to your branch in a file called `prime_scraper.py`.  The format of your branch name should be as follows: f"{last_name}_{first_name}".  IE - If your name is "John Smith", your branch name should be `smith_john`.*

---

**EXAMPLE/REFERENCE LIST:**

```python
[{'discounted-price': '$6.39',
  'list-price': '$7.99',
  'product-link': 'https://www.amazon.com/Kitsch-Scrunchies-Accessories-Fashion-Blacks/dp/B0799X7Z15?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B0799X7Z15&ref_=deb_tdp_ss_ee_B0799X7Z15',
  'product-name': "Kitsch Scrunchies for Women's Hair - Metallic Hair "
                  'Scrunchies | Large Hair Ties for Women | Hair Tie '
                  'Scrunchies for Girls | Cute Scrunchie | Hair Bands & '
                  'Ponytail Holders, 5pc (Metallic BlackGray)'},
 {'discounted-price': '$22.79',
  'list-price': '$27.89',
  'product-link': 'https://www.amazon.com/Biotin-Vitamins-Collagen-Keratin-Supplement/dp/B09RKDGYJD?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B09RKDGYJD&ref_=deb_tdp_ss_ee_B09RKDGYJD',
  'product-name': 'Biotin | Collagen | Keratin | Hyaluronic Acid - Hair Growth '
                  'Support Supplement | Skin & Nails Beauty Complex 25000 mcg '
                  '- B1 | B2 | B3 | B6 | B7 - Made in USA - For Women & Men | '
                  '60 Capsules'},
 {'discounted-price': '$33.98',
  'list-price': '$43.99',
  'product-link': 'https://www.amazon.com/Valuetoner-Compatible-Cartridge-Replacement-Pg-245Xl/dp/B07TJ87YKB?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B07TJ87YKB&ref_=deb_tdp_ss_ee_B07TJ87YKB',
  'product-name': 'Valuetoner Ink Cartridge Replacement for Canon 245XL/black '
                  'and The 246xl/Color 243 244 Combo Pack for Pixma TR4520 '
                  'TR4527 MG2522 MG2520 MX490 MX492 TS202 TS302 TS3320 MG2920 '
                  'Printer (Black, Color)'},
 {'discounted-price': '$8.58',
  'list-price': '$12.99',
  'product-link': 'https://www.amazon.com/Charcoal-Loofahs-Essential-Whale-Life/dp/B07L64SWDR?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B07L64SWDR&ref_=deb_tdp_ss_ee_B07L64SWDR',
  'product-name': 'Shower Puff 4 Pack Black Bath Sponge Shower Loofahs Pouf '
                  'Ball Nature Bamboo Charcoal Mesh Bulk Puffs Large, Shower '
                  'Essential Skin Care by WhaleLife'},
 {'discounted-price': '$25.52',
  'list-price': '$33.59',
  'product-link': 'https://www.amazon.com/Fresh-Step-Advanced-Extreme-Clumping/dp/B07ZK3NSJQ?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B07ZK3NSJQ&ref_=deb_tdp_ss_ee_B07ZK3NSJQ',
  'product-name': 'Fresh Step Clumping Cat Litter, Extreme, Advanced Long '
                  'Lasting Odor Control Kitty Litter with Activated Charcoal, '
                  'Low Dust Formula, 37 lb'},
 {'discounted-price': '$11.19',
  'list-price': '$19.99',
  'product-link': 'https://www.amazon.com/Kitsch-Strengthening-Shampoo-All-Natural-Moisturizing/dp/B09FB1YXF1?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B09FB1YXF1&ref_=deb_tdp_ss_ee_B09FB1YXF1',
  'product-name': 'Kitsch Rice Water Shampoo Bar for Hair Growth | Vegan & All '
                  'Natural Hair Growth Shampoo Bar | Made in US | Rice Shampoo '
                  'Bar for Strengthening Weak or Damaged Hair | Paraben Free | '
                  'Sulfate Free, 3.2oz'},
 {'discounted-price': '$29.69',
  'list-price': '$32.99',
  'product-link': 'https://www.amazon.com/Reli-EcoStretch-Compostable-Trash-30-33/dp/B07V5BM2L1?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B07V5BM2L1&ref_=deb_tdp_ss_ee_B07V5BM2L1',
  'product-name': 'Reli. Compostable 33 Gallon Trash Bags | 40 Count | ASTM '
                  'D6400 | Green | Eco-Friendly | For Compost'},
 {'discounted-price': '$32.94',
  'list-price': '$38.97',
  'product-link': 'https://www.amazon.com/Aloderma-Organic-Certified-Harvest-Suitable/dp/B0B8F42QRB?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B0B8F42QRB&ref_=deb_tdp_ss_ee_B0B8F42QRB',
  'product-name': 'Aloderma Organic Aloe Vera Gel for Face Made within 12 '
                  'Hours of Harvest, 96% Pure Aloe Vera Gel for Skin, Scalp, & '
                  'Hair, Soothing Aloe Face Moisturizer, Multipurpose, '
                  'Hydrating Aloe Gel, 7oz, 3-Pack'},
 {'discounted-price': '$23.79',
  'list-price': '$27.99',
  'product-link': 'https://www.amazon.com/Kitsch-Conditioner-Strengthening-Cleansing-Moisturizing/dp/B0BS2D2KN7?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B0BS2D2KN7&ref_=deb_tdp_ss_ee_B0BS2D2KN7',
  'product-name': 'Kitsch Rice Bar Shampoo and Conditioner Bar for Hair Growth '
                  '| Made in US | Rice Shampoo Bar & Conditioner Bar for '
                  'Strengthening Hair | Rice Water Shampoo Bar & Conditioner '
                  'Soap | Paraben Free, 2pc Set'},
 {'discounted-price': '$6.79',
  'list-price': '$7.99',
  'product-link': 'https://www.amazon.com/Kitsch-Scrunchies-Scrunchie-Prevention-Preservation/dp/B0798RWHC9?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B0798RWHC9&ref_=deb_tdp_ss_ee_B0798RWHC9',
  'product-name': 'Kitsch Satin Hair Scrunchies for Women - Softer Than Silk '
                  'Scrunchies for Hair | Satin Scrunchies for Girls | Satin '
                  'Hair Ties for Women | Silk Hair Ties No Damage | Silk '
                  'Ponytail Holders, 5 pcs (Black)'},
 {'discounted-price': '$16.14',
  'list-price': '$21.99',
  'product-link': 'https://www.amazon.com/Little-Remedies-Essentials-Featuring-Boudreauxs/dp/B075G6XMSF?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B075G6XMSF&ref_=deb_tdp_ss_ee_B075G6XMSF',
  'product-name': 'Little Remedies, New Baby Essentials Kit, 6 Newborn '
                  'Essentials, Saline Nasal Spray, Gas Relief Drops, Gripe '
                  'Water, Fever Reliever, & Diaper Ointment'},
 {'discounted-price': '$24.99',
  'list-price': '$39.99',
  'product-link': 'https://www.amazon.com/Biotin-Anti-Hair-Loss-Shampoo/dp/B07K4S4J66?pd_rd_w=QnYLG&content-id=amzn1.sym.f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_p=f369f4c6-92a1-41f4-a499-9526fbf5a040&pf_rd_r=0JP40GWN3QAGA5375NWM&pd_rd_wg=zGG83&pd_rd_r=a0a03be5-df1a-4610-9de1-c9b09b479d58&pd_rd_i=B07K4S4J66&ref_=deb_tdp_ss_ee_B07K4S4J66',
  'product-name': 'Biotin Shampoo and Conditioner Set - Sulfate and Paraben '
                  'Free Treatment for Men and Women - Hair Thickening '
                  'Volumizing Products to Help Boost Thinning Hair with Added '
                  'Keratin'}]
```
