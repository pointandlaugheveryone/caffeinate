#### A web app to help caffeine addicts like me save money.
- Displays caffeinated drinks currently on sale in most popular czech grocery stores.
- filtering based on sugar content (in case your lifestyle is not unhealthy enough), dark mode included
- proudly used minimum amount of javascript
\
\
For parsing the sale data I used [pykupi](https://github.com/prostmich/pykupi) with slight changes in [my fork](https://github.com/pointandlaugheveryone/pykupi)

---
TODO:
- [x] track amount of drinks as well (would break the current version)
- [ ] sale until [date] 
- [ ] rewrite db strcture to associate drinks with their respective zero versions
- [ ] individual page for all drinks displaying all offers && for all stores displaying sales in them (many-to-many table)
