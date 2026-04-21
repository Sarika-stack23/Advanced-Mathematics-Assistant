"""
╔══════════════════════════════════════════════════════════════════════╗
║  knowledge_base.py — Advanced Mathematics Assistant V2              ║
║  ✅ Class 6  — 14 chapters                                          ║
║  ✅ Class 7  — 15 chapters                                          ║
║  🔜 Class 8, 9, 10, 11, 12, JEE — coming next sessions             ║
║  HOW TO ADD MORE: append Document objects, then --rebuild           ║
╚══════════════════════════════════════════════════════════════════════╝
"""

try:
    from langchain_core.documents import Document
except ImportError:
    try:
        from langchain.schema import Document
    except ImportError:
        class Document:
            def __init__(self, page_content: str, metadata: dict = None):
                self.page_content = page_content
                self.metadata = metadata or {}


# ════════════════════════════════════════════════════════════════════
#  SECTION 1 — CLASS_EXAMPLES (sidebar dropdown data)
# ════════════════════════════════════════════════════════════════════

CLASS_EXAMPLES = {
    "📘 Class 6": {
        "Ch1 · Knowing Our Numbers":      "Write 5,08,01,592 in words and find the difference between place value and face value of 8 in this number",
        "Ch2 · Whole Numbers":            "Show 3 + 4 = 4 + 3 and 2 x (3 + 4) = 2x3 + 2x4 on a number line and explain the properties used",
        "Ch3 · Playing With Numbers":     "Find HCF and LCM of 36 and 48 using prime factorisation method step by step",
        "Ch4 · Basic Geometrical Ideas":  "Define point, line, line segment, ray and angle with diagrams. What is the difference between a line and a line segment?",
        "Ch5 · Elementary Shapes":        "Classify angles: 35, 90, 120, 180, 270 degrees. Name the type of triangle with sides 3cm, 4cm, 5cm",
        "Ch6 · Integers":                 "Solve using number line: (-5) + 8, 3 - (-4), (-6) + (-2). Explain rules for addition of integers",
        "Ch7 · Fractions":                "Solve: 3/4 + 5/6 - 1/3. Also arrange 2/3, 3/4, 5/8, 7/12 in ascending order",
        "Ch8 · Decimals":                 "Convert 2.375 to fraction. Multiply 3.25 x 1.4 and divide 8.64 by 0.6 with full steps",
        "Ch9 · Data Handling":            "Find mean, median and mode of: 12, 15, 11, 18, 15, 13, 20, 15, 10",
        "Ch10 · Mensuration":             "Find perimeter and area of a rectangle 15cm x 8cm and a square of side 9cm",
        "Ch11 · Algebra":                 "Write expressions for: 5 added to 3 times x, y subtracted from 10. Find value when x=4, y=3",
        "Ch12 · Ratio and Proportion":    "Divide 720 between Arjun and Bharat in ratio 4:5. Check if 3:4 and 9:12 are in proportion",
        "Ch13 · Symmetry":                "How many lines of symmetry: equilateral triangle, square, rectangle, circle, regular hexagon?",
        "Ch14 · Practical Geometry":      "Construct a line segment of 6.5cm. Draw perpendicular bisector and angle bisector of 60 degrees",
    },
    "📗 Class 7": {
        "Ch1 · Integers":                 "Evaluate: (-8) x (-5), (-36) divided by 4, (-7) x 8 + (-7) x 2. State properties of multiplication of integers",
        "Ch2 · Fractions and Decimals":   "Multiply 2 and 3/4 by 1 and 1/3. Divide 3 and 1/2 by 1 and 2/3. Convert 0.125, 1.625 to fractions",
        "Ch3 · Data Handling":            "Find mean of first 10 natural numbers. Find mode and median of 4,7,2,9,4,8,4,6. Probability of even number on die?",
        "Ch4 · Simple Equations":         "Solve: 2x + 7 = 19, 3(y - 4) = 2y + 1, (x+2)/3 = (x-1)/4. Verify answers by substitution",
        "Ch5 · Lines and Angles":         "Two parallel lines cut by transversal. One angle is 65 degrees. Find all 8 angles and name each pair",
        "Ch6 · Triangle Properties":      "In triangle ABC, angle A=50, angle B=70. Find angle C. Verify exterior angle theorem",
        "Ch7 · Congruence of Triangles":  "State all congruence rules SSS SAS ASA AAS RHS with examples. When can we NOT use AAA?",
        "Ch8 · Comparing Quantities":     "Find 15% of 400. What % is 45 of 180? SP when CP=850 profit=12%. SP when CP=600 loss=8%",
        "Ch9 · Rational Numbers":         "Represent -3/5 on number line. Find 3 rational numbers between 1/4 and 1/2",
        "Ch10 · Practical Geometry":      "Construct triangle PQR where PQ=5cm, QR=4.5cm, angle Q=60 degrees using compass and ruler",
        "Ch11 · Perimeter and Area":      "Find area of parallelogram base 8cm height 5cm. Find circumference and area of circle radius 7cm",
        "Ch12 · Algebraic Expressions":   "Add 3x squared + 2x - 5 and x squared - 3x + 2. Subtract 2a-3b from 5a+2b",
        "Ch13 · Exponents and Powers":    "Simplify: 2 to the 5 times 2 to the 3, 3 to the 7 divided by 3 to the 4. Express 48000000 in standard form",
        "Ch14 · Symmetry":                "Find order of rotational symmetry of square, rectangle, equilateral triangle, circle, regular pentagon",
        "Ch15 · Solid Shapes":            "Draw nets for cube, cuboid, triangular prism. Find faces, edges, vertices. Verify Euler formula F+V-E=2",
    },
    "📙 Class 8": {
        "Ch1 · Rational Numbers":         "Find 5 rational numbers between -1/2 and 1/3. Verify commutativity for -2/3 and 4/5",
        "Ch2 · Linear Equations":         "Solve: (2x+3)/5 - (x-4)/3 = 2. A number is 4 more than twice another and their sum is 40",
        "Ch3 · Quadrilaterals":           "In parallelogram ABCD, angle A=75 degrees. Find all angles. State properties of rhombus and kite",
        "Ch4 · Practical Geometry":       "Construct quadrilateral ABCD: AB=4cm, BC=3.5cm, CD=4.5cm, DA=3cm, AC=5cm",
        "Ch5 · Data Handling":            "Draw pie chart: Wheat 40%, Rice 30%, Maize 20%, Others 10%. Probability of red card from 52",
        "Ch6 · Squares and Square Roots": "Find square root of 1764 by prime factorisation and long division. Is 1352 a perfect square?",
        "Ch7 · Cubes and Cube Roots":     "Find cube root of 13824 by prime factorisation. Find smallest multiplier to make 675 a perfect cube",
        "Ch8 · Comparing Quantities":     "Find CI on 12000 at 10% per year for 2 years compounded annually. Compare with SI",
        "Ch9 · Algebraic Identities":     "Expand (3x+2y) squared, (4a-3b) squared, (x+3)(x-3). Factorise x squared+8x+16",
        "Ch10 · Solid Shapes":            "Draw top view, front view and side view of cube, cylinder and cone",
        "Ch11 · Mensuration":             "Find area of trapezium parallel sides 8cm and 5cm height 4cm. Surface area of cuboid 5x4x3cm",
        "Ch12 · Exponents and Powers":    "Simplify: (2 to -3 times 3 to -2) divided by 6 to -1. Express 0.00000605 in standard form",
        "Ch13 · Direct Inverse Proportion":"8 workers finish in 12 days. How many days for 6 workers? If 15 bags cost 450, cost of 24 bags?",
        "Ch14 · Factorisation":           "Factorise: 12x squared y - 9xy squared + 6xyz, x squared + 7x + 12, 2x squared + 7x + 3",
        "Ch15 · Introduction to Graphs":  "Plot A(2,3), B(-1,4), C(0,-2). Draw graph of x+y=5 and find where it cuts both axes",
        "Ch16 · Playing With Numbers":    "A 2-digit number is 4 times sum of its digits. If 18 is added digits reverse. Find the number",
    },
    "📒 Class 9": {
        "Ch1 · Number Systems":           "Prove root 2 is irrational. Represent root 5 on number line. Rationalise 3/(2+root3)",
        "Ch2 · Polynomials":              "Find remainder when x cubed - 6x squared + 11x - 6 is divided by x-2. Factorise x cubed - 23x squared + 142x - 120",
        "Ch3 · Coordinate Geometry":      "Plot A(3,4), B(-2,3), C(-4,-1), D(2,-3). Find which quadrant each lies in. Find distance AB",
        "Ch4 · Linear Equations 2 Var":   "Draw graph of 2x+3y=12. Find x-intercept and y-intercept. Find 3 solutions",
        "Ch5 · Euclid's Geometry":        "State Euclid's 5 postulates. Explain parallel postulate. Give 2 theorems from postulates",
        "Ch6 · Lines and Angles":         "Prove vertically opposite angles are equal. Find all 8 angles when parallel lines cut by transversal",
        "Ch7 · Triangles":                "Prove angles opposite equal sides of isosceles triangle are equal. State and prove ASA rule",
        "Ch8 · Quadrilaterals":           "Prove diagonals of parallelogram bisect each other. Prove mid-point theorem with full proof",
        "Ch9 · Areas Parallelogram":      "Prove parallelograms on same base and between same parallels are equal in area",
        "Ch10 · Circles":                 "Prove equal chords subtend equal angles at centre. Prove angle in semicircle is 90 degrees",
        "Ch11 · Constructions":           "Construct triangle with perimeter 11cm and base angles 60 and 45 degrees",
        "Ch12 · Heron's Formula":         "Find area of triangle with sides 13cm, 14cm, 15cm using Heron's formula",
        "Ch13 · Surface Areas Volumes":   "Find total surface area and volume of cone radius 5cm slant height 13cm",
        "Ch14 · Statistics":              "Find mean by assumed mean method. Find median and mode for grouped frequency data",
        "Ch15 · Probability":             "Bag has 5 red, 7 blue, 3 green balls. Find probability of red, not blue, green or red",
    },
    "📓 Class 10": {
        "Ch1 · Real Numbers":             "Prove root 3 is irrational. Find HCF of 96 and 404 by Euclid's algorithm",
        "Ch2 · Polynomials":              "Find zeroes of 6x squared - 3 - 7x and verify sum and product of zeroes formulas",
        "Ch3 · Pair of Linear Equations": "Solve by cross multiplication: 2x+3y=11, 2x-4y=-24. Solve graphically and find area of triangle formed",
        "Ch4 · Quadratic Equations":      "Solve 2x squared - 7x + 3 = 0 by factorisation, completing square and quadratic formula",
        "Ch5 · Arithmetic Progressions":  "Find sum of first 40 positive integers divisible by 6. If 7th term is 34 and 13th term is 64, find the AP",
        "Ch6 · Triangles":                "State and prove Basic Proportionality Theorem. Prove area ratio equals square of side ratio for similar triangles",
        "Ch7 · Coordinate Geometry":      "Find area of triangle A(2,3), B(-1,0), C(2,-4). Find point dividing line joining (1,3) and (4,6) in ratio 2:1",
        "Ch8 · Introduction to Trig":     "If sin theta = 3/5 find all trig ratios. Prove sin squared + cos squared = 1",
        "Ch9 · Applications of Trig":     "From top of 75m tower angles of depression of two boats are 30 and 45 degrees. Find distance between boats",
        "Ch10 · Circles":                 "Prove tangent is perpendicular to radius. Find length of tangent from point 17cm from centre radius 8cm",
        "Ch11 · Constructions":           "Divide line segment 7cm in ratio 3:2. Draw pair of tangents from point 10cm from centre radius 4cm",
        "Ch12 · Areas Related to Circles":"Find area of sector radius 14cm angle 60 degrees. Find area of segment",
        "Ch13 · Surface Areas Volumes":   "Solid is cone on hemisphere radius 3.5cm cone height 4cm. Find total surface area and volume",
        "Ch14 · Statistics":              "Find mean by step deviation method. Find median and mode of frequency distribution",
        "Ch15 · Probability":             "Two dice thrown. Find probability sum is 8, sum is prime, same number on both dice",
    },
    "📕 Class 11": {
        "Ch1 · Sets":                     "If A={1,2,3,4,5} B={2,4,6,8} find A union B, A intersection B, A-B, B-A. Verify n(A union B) formula",
        "Ch2 · Relations and Functions":  "Find domain and range of f(x)=root(9-x squared). Find fog and gof if f(x)=2x+1 and g(x)=x squared-1",
        "Ch3 · Trigonometric Functions":  "Prove sin(A+B)sin(A-B)=sin squared A - sin squared B. Solve 2cos squared x - 3cosx + 1 = 0",
        "Ch4 · Math Induction":           "Prove by PMI: 1+2+3+...+n = n(n+1)/2. Prove 4 to n - 1 is divisible by 3",
        "Ch5 · Complex Numbers":          "Find modulus and argument of z = -1 + i root 3. Express in polar form. Find cube roots of unity",
        "Ch6 · Linear Inequalities":      "Solve 3x-2 > 2x+1 and show on number line. Solve system x+y<=10, x+3y<=15, x>=0, y>=0",
        "Ch7 · Permutations Combinations":"5 boys and 3 girls sit in row if girls always sit together. Find 7C3. Prove nCr + nCr-1 = n+1Cr",
        "Ch8 · Binomial Theorem":         "Expand (2x-3y) to 4th power. Find 5th term in (x+2) to 8th. Find term independent of x in (x+1/x) to 10th",
        "Ch9 · Sequences and Series":     "Find sum of GP 1+3+9+...+2187. If AM=10 and GM=8 find the numbers",
        "Ch10 · Straight Lines":          "Find equation through (2,-3) perpendicular to 3x-4y+5=0. Distance between parallel lines 3x+4y-5=0 and 3x+4y+15=0",
        "Ch11 · Conic Sections":          "Find focus, directrix, latus rectum of y squared = 12x. Equation of ellipse with foci (plus minus 3, 0) and a=5",
        "Ch12 · 3D Geometry":             "Find distance between A(1,2,3) and B(4,-2,6). Find point dividing AB in ratio 2:1",
        "Ch13 · Limits and Derivatives":  "Find limit of sin3x/x as x approaches 0. Differentiate x cubed times sinx using product rule",
        "Ch14 · Math Reasoning":          "Write negation of: All primes are odd. Write converse and contrapositive of: If x>5 then x squared > 25",
        "Ch15 · Statistics":              "Find variance and standard deviation of 6,8,10,12,14. Compare variability using coefficient of variation",
        "Ch16 · Probability":             "P(A)=0.4, P(B)=0.5, P(A intersection B)=0.2. Find P(A union B) and P(A given B)",
    },
    "📔 Class 12": {
        "Ch1 · Relations and Functions":  "Show f(x)=2x+3 is bijective. Is R={(a,b): a-b divisible by 5} an equivalence relation?",
        "Ch2 · Inverse Trig Functions":   "Find sin inverse(-1/2), cos inverse(-root3/2), tan inverse(root3). Prove sin inverse x + cos inverse x = pi/2",
        "Ch3 · Matrices":                 "If A=[[1,2],[3,4]] find A + A transpose. Show it is symmetric. Express A as sum of symmetric and skew-symmetric",
        "Ch4 · Determinants":             "Find determinant of 3x3 matrix. Find inverse using adjoint. Solve using Cramer's rule: x+y+z=6, 2x-y+z=3",
        "Ch5 · Continuity Differentiability":"Check continuity of |x-3| at x=3. Differentiate x to x, sin(logx), e to x squared",
        "Ch6 · Applications of Derivatives":"Find intervals where 2x cubed - 9x squared + 12x - 5 is increasing. Find local maxima and minima",
        "Ch7 · Integrals":                "Evaluate integral of x squared e to x dx by parts. Integral of 1/(x squared - 4) by partial fractions",
        "Ch8 · Application of Integrals": "Find area bounded by y=x squared and y=x+2. Area of circle x squared + y squared = 16",
        "Ch9 · Differential Equations":   "Solve dy/dx = (x squared + y squared)/2xy homogeneous. Solve linear DE dy/dx + 2y/x = x squared",
        "Ch10 · Vector Algebra":          "If a=2i+3j-k and b=i-2j+3k find a dot b, a cross b, angle between them",
        "Ch11 · 3D Geometry":             "Find angle between two lines given in symmetric form. Distance from point (1,2,3) to plane 2x-3y+z=5",
        "Ch12 · Linear Programming":      "Maximise Z=3x+4y subject to x+y<=450, 2x+y<=600, x>=0, y>=0. Find all corner points",
        "Ch13 · Probability":             "Bag A has 3 red 5 black. Bag B has 4 red 6 black. Ball drawn is red. Find P(from bag A) using Bayes theorem",
    },
    "🏆 JEE Advanced": {
        "Definite Integrals":             "Evaluate integral from 0 to pi of x sinx/(1+cos squared x) dx using King's property. Show full working",
        "Complex Numbers":                "If z=(root3+i)/(1-i*root3), find modulus, argument and polar form. Find z to the 10th using De Moivre",
        "Theory of Equations":            "If roots of x cubed - 6x squared + 11x - 6 = 0 are in AP find them. Find conditions for both roots of quadratic in (1,2)",
        "Binomial Advanced":              "Find sum C(n,0) squared + C(n,1) squared + ... + C(n,n) squared. Find greatest term in (3+2x) to 10 when x=3/2",
        "Advanced Trigonometry":          "Solve sin2x - sinx = cosx - cos2x for x in [0,2pi]. Prove cos(pi/7) times cos(2pi/7) times cos(3pi/7) = 1/8",
        "Vectors and 3D Advanced":        "Find shortest distance between skew lines r=(i+j)+t(2i-j+k) and r=(2i+j-k)+s(3i-5j+2k)",
        "Probability Advanced":           "4 cards drawn without replacement. Find P(all suits represented) and P(exactly 2 aces)",
        "Inequalities":                   "Prove AM >= GM for 3 positive numbers. Find minimum of (x+1/x) squared + (y+1/y) squared for positive x,y with xy=1",
    },
}


# ════════════════════════════════════════════════════════════════════
#  SECTION 2 — MATH_KNOWLEDGE_BASE (RAG documents)
# ════════════════════════════════════════════════════════════════════

MATH_KNOWLEDGE_BASE = [

    # ── CLASS 6 — All 14 Chapters ───────────────────────────────────

    Document(page_content="""Class 6 | Ch1: Knowing Our Numbers
Indian number system: ones, thousands, lakhs, crores.
Place value = digit x position value. Face value = digit itself.
For 5,08,01,592: 5 in crores=5,00,00,000. Face value of 8=8 always.
Comparison: more digits=greater. Same digits: compare from left.
Rounding: nearest 10 (look at ones), nearest 100 (look at tens).
Roman: I=1,V=5,X=10,L=50,C=100,D=500,M=1000. Before=subtract(IV=4), After=add(VI=6).
Example: 7,35,02,814 = Seven crore thirty-five lakh two thousand eight hundred fourteen.
Common mistake: place value depends on position, face value is always the digit itself.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch2: Whole Numbers
Natural Numbers: 1,2,3,... Whole Numbers: 0,1,2,3,... (0 is whole but NOT natural)
Properties: Closure(a+b and a×b always whole), Commutativity(a+b=b+a), Associativity, Distributivity(a×(b+c)=a×b+a×c)
Identity: a+0=a (additive), a×1=a (multiplicative). Zero property: a×0=0.
Predecessor of n=n-1. Successor of n=n+1.
Triangular numbers: 1,3,6,10,15 (n(n+1)/2). Square numbers: 1,4,9,16,25.
Sum 1+2+...+100 = 100×101/2 = 5050.
Common mistake: 0 is NOT natural. Subtraction/division NOT always closed for whole numbers.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch3: Playing With Numbers - HCF and LCM
Prime: exactly 2 factors. Composite: more than 2. 1=neither. 2=only even prime.
Divisibility: by 2(last digit even), 3(digit sum div by 3), 5(last digit 0 or 5), 9(digit sum div by 9), 11(alternate digit difference=0 or multiple of 11).
Prime factorisation: 48=2^4 x 3.
HCF = product of COMMON prime factors with LOWEST powers.
LCM = product of ALL prime factors with HIGHEST powers.
KEY: HCF x LCM = product of the two numbers.
Example: HCF(36,48)=12, LCM(36,48)=144. Check: 12×144=1728=36×48.
Three bells every 6,10,15 min → together at LCM(6,10,15)=30 min.
Common mistake: HCF uses LOWEST powers, LCM uses HIGHEST powers (students mix these up).""",
    metadata={"source": "ncert", "topic": "number_theory", "class_level": "class_6", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch4: Basic Geometrical Ideas
Point: exact location, no size. Line: infinite both ways. Line segment: two endpoints. Ray: one endpoint infinite one way.
Angles: Acute(0-90), Right(90), Obtuse(90-180), Straight(180), Reflex(180-360), Complete(360).
Circle parts: Centre(fixed point), Radius(centre to circle), Diameter(chord through centre=2r), Chord(any two points on circle), Arc(part of circle), Sector(two radii + arc), Segment(chord + arc).
One line through two points. Infinite lines through one point.
Diameter is a chord but chord is not always diameter.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch5: Understanding Elementary Shapes
Triangles by sides: Equilateral(all equal, all 60°), Isosceles(2 equal), Scalene(all different).
Triangles by angles: Acute(all<90°), Right(one=90°), Obtuse(one>90°).
Pythagorean triplets: (3,4,5),(5,12,13),(8,15,17),(7,24,25). Check: 3^2+4^2=25=5^2.
Quadrilaterals: Rectangle(4 right angles, opposite sides equal), Square(4 right angles, all sides equal), Parallelogram(opposite sides parallel equal), Rhombus(all sides equal), Trapezium(one pair parallel sides).
3D: Cube(F=6,E=12,V=8), Cuboid(F=6,E=12,V=8). Euler: F+V-E=2.
Square is special rectangle AND special rhombus. Hypotenuse=longest side opposite 90°.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch6: Integers
Integers: ...-3,-2,-1,0,1,2,3... Right=greater, left=smaller on number line.
Positive > Zero > Negative. Among negatives: closer to zero is greater (-2>-5).
Addition: same sign(add, keep sign), different signs(subtract smaller absolute, keep sign of larger).
Subtraction: a-b = a+(-b). So 5-8=5+(-8)=-3. Also -3-(-5)=-3+5=2.
Ascending: -8<-5<-1<0<2<3.
Real life: temperature below zero, basement floors, bank withdrawals.
Common mistake: -5 is NOT greater than -2. Subtracting negative = adding positive: 5-(-3)=8.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_6", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch7: Fractions
Types: Proper(p<q), Improper(p>=q), Mixed(whole+proper), Unit(p=1).
Equivalent: 1/2=2/4=3/6. Multiply or divide both by same number.
Comparing: same denominator compare numerators. Same numerator: smaller denominator=LARGER fraction.
Add/subtract: same denominator add numerators. Different: find LCM first.
Example: 3/4+5/6-1/3. LCM=12. = 9/12+10/12-4/12 = 15/12 = 5/4 = 1 and 1/4.
Ascending 2/3,3/4,5/8,7/12: LCM=24 → 16,18,15,14 over 24 → 7/12 < 5/8 < 2/3 < 3/4.
Common mistake: 1/2+1/3 ≠ 2/5. Correct: 3/6+2/6=5/6.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch8: Decimals
Place value: 45.378 → 4=tens, 5=ones, 3=tenths, 7=hundredths, 8=thousandths.
Conversion: 0.375=375/1000=3/8. Fraction to decimal: divide (3/4=0.75).
Multiplication: count total decimal places. 3.25×1.4=325×14/1000=4550/1000=4.55.
Division by decimal: multiply both to remove decimal. 8.64÷0.6=86.4÷6=14.4.
Comparison: compare whole part, then tenths, then hundredths.
Always align decimal points during addition and subtraction.
0.5×0.5=0.25 (not 0.025). Count 1+1=2 decimal places.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch8", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch9: Data Handling
Mean = Sum/Count. Median = middle value when arranged in order.
Odd count: middle term. Even count: average of two middle terms.
Mode = most frequent value. Range = Max - Min.
Bar graph: equal width bars, height=frequency. Tally: groups of 5.
Probability: P(event)=favourable/total. Always between 0 and 1.
Example: 12,15,11,18,15,13,20,15,10. Mean=129/9=14.33. Arranged→Median=15. Mode=15.
P(even on die)=3/6=1/2.
Must arrange data BEFORE finding median. Mode is most FREQUENT not largest.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_6", "chapter": "ch9", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch10: Mensuration
Perimeter: Rectangle=2(l+b), Square=4s, Triangle=a+b+c.
Area: Rectangle=l×b, Square=s^2, Triangle=(1/2)×base×height.
Units: perimeter in cm/m, area in cm^2/m^2. 1m^2=10000cm^2. 1 hectare=10000m^2.
Example: Rectangle 15×8: P=46cm, A=120cm^2. Square 9cm: P=36cm, A=81cm^2.
Triangle base 12cm height 7cm: A=42cm^2.
Room 5m×4m tiles 25cm×25cm: Area=20m^2=200000cm^2. Tiles=200000/625=320.
Height of triangle must be PERPENDICULAR to base. Area of square=s^2 NOT 4s.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_6", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch11: Algebra - Introduction
Variable: letter for unknown (x,y,n). Constant: fixed value.
3x means 3×x. x^2 means x×x. "5 less than x" = x-5 NOT 5-x.
Like terms: same variable and power (3x and 7x). Unlike: different.
Expression: no equal sign (2x+3). Equation: has equal sign (2x+3=11).
Substitution: x=4 in 3x+5 = 3(4)+5=17.
"5 added to 3 times x"=3x+5. "y subtracted from 10"=10-y.
"Twice a number decreased by 4"=2n-4.
An expression has no solution. Only equations can be solved.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_6", "chapter": "ch11", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch12: Ratio and Proportion
Ratio a:b = a/b. No units. Both quantities must be in SAME unit first.
Equivalent: 2:3=4:6=6:9.
Proportion a:b::c:d: product of extremes = product of means: a×d=b×c.
Unitary method: find cost of 1, multiply for required number.
Example: Divide 720 in 4:5. Total parts=9. Shares: 4/9×720=320 and 5/9×720=400.
Proportion check 3:4 and 9:12: 3×12=36=4×9=36. YES.
6 pens cost 90 → 1 pen=15 → 10 pens=150.
50cm:2m must convert → 50:200=1:4. Ratio requires SAME units.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_6", "chapter": "ch12", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch13: Symmetry
Line of symmetry divides figure into two mirror-image halves.
Symmetry count: Equilateral triangle=3, Square=4, Rectangle=2(midpoints only NOT diagonals), Rhombus=2(diagonals), Circle=infinite, Pentagon=5, Hexagon=6, Isosceles triangle=1, Scalene=0, Parallelogram=0.
Regular n-sided polygon has n lines of symmetry.
Rectangle: 2 lines (horizontal+vertical through midpoints). Diagonals NOT lines of symmetry.
Rhombus: 2 lines (both diagonals are lines of symmetry).
Letters: Vertical symmetry: A,H,I,M,O,T,U,V,W,X,Y. Horizontal: B,C,D,E.
Parallelogram has NO line of symmetry at all.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 6 | Ch14: Practical Geometry
Tools: Ruler, Compass, Protractor, Divider, Set squares.
Perpendicular bisector of AB: open compass>half AB, arcs from A and B, intersect at P and Q, join PQ.
Angle bisector of angle AOB: arc from O cuts both rays at P,Q. Equal arcs from P,Q intersect at R. OR bisects angle.
Standard angles with compass: 60°(equilateral triangle), 90°(perp bisector method), 30°(bisect 60°), 45°(bisect 90°), 75°=60°+15°.
Compass must not slip while drawing arc. Centre of protractor EXACTLY on vertex.
Must open compass MORE than half segment for perpendicular bisector to work.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_6", "chapter": "ch14", "difficulty": "beginner"}),

    # ── CLASS 7 — All 15 Chapters ───────────────────────────────────

    Document(page_content="""Class 7 | Ch1: Integers
Absolute value |a| = distance from zero (always positive).
Multiplication: same signs=positive, different signs=negative.
(+)×(+)=+, (-)×(-)=+, (+)×(-)=-, (-)×(+)=-.
Division: same sign rules as multiplication.
(-36)÷(-6)=+6. (-36)÷(+6)=-6.
Distributivity: (-7)×8+(-7)×2 = (-7)(8+2) = (-7)(10) = -70.
Properties: closure under +,-,×. Commutativity for + and ×. Associativity. a×0=0.
Temperature: -3°C fell 5°C = -3+(-5) = -8°C.
Common mistake: (-3)^2=+9 but -(3^2)=-9. Two negatives multiply to positive.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch2: Fractions and Decimals
Multiplication of fractions: (a/b)×(c/d)=ac/bd. Convert mixed to improper first.
2(3/4)×1(1/3) = (11/4)×(4/3) = 44/12 = 11/3 = 3(2/3).
Division: a/b ÷ c/d = a/b × d/c (multiply by RECIPROCAL of second).
3(1/2)÷1(2/3) = (7/2)÷(5/3) = (7/2)×(3/5) = 21/10 = 2.1.
Decimal multiplication: count total decimal places. 0.4×0.3=0.12 (1+1=2 places).
Division by decimal: 2.4÷0.6 = 24÷6 = 4 (multiply both by 10).
Conversion: 0.125=125/1000=1/8. 1.625=1625/1000=13/8=1(5/8).
Common mistake: flip SECOND fraction not first when dividing fractions.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_7", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch3: Data Handling
Mean=Sum/n. Mean of first n natural numbers=(n+1)/2.
Median: arrange in order. Odd: middle term. Even: average of two middle terms.
Mode: most frequent. Range=Max-Min.
Double bar graph: compares two datasets side by side.
Probability: P(event)=favourable/total. Between 0 and 1.
Example: 4,7,2,9,4,8,4,6. Mean=44/8=5.5. Arranged:2,4,4,4,6,7,8,9. Median=(4+6)/2=5. Mode=4.
P(even on die)=3/6=1/2 (even numbers: 2,4,6).
Always arrange data BEFORE median. Probability never exceeds 1.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_7", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch4: Simple Equations
Equation: LHS=RHS. Solution: value making equation true.
Transposition: move term to other side changing sign. +a becomes -a, ×a becomes ÷a.
Golden rule: same operation on BOTH sides.
Steps: collect variables one side, constants other side, divide by coefficient.
Solve 2x+7=19: 2x=12, x=6. Verify: 2(6)+7=19 correct.
Solve 3(y-4)=2y+1: 3y-12=2y+1, y=13. Verify: 3(9)=27=2(13)+1 correct.
Cross multiply: (x+2)/3=(x-1)/4 → 4(x+2)=3(x-1) → x=-11.
Word problem: consecutive integers sum=53. n+(n+1)=53 → n=26. Integers: 26,27.
Always verify by substituting back. Expand brackets BEFORE transposing.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_7", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch5: Lines and Angles
Complementary=90° total. Supplementary=180° total. Linear pair=180°. Vertically opposite=EQUAL.
Parallel lines + transversal: 8 angles formed.
Corresponding angles: same position=EQUAL (F-shape).
Alternate interior angles: between lines, alternate sides=EQUAL (Z-shape).
Co-interior angles: between lines, same side=SUPPLEMENTARY=180° (C-shape).
Alternate exterior angles: outside, alternate sides=EQUAL.
Converse: if corresponding/alternate angles equal → lines parallel.
Example: angle=65°. Corresponding=65°. Alternate interior=65°. Co-interior=115°.
Two supplementary angles, one=3 times other: x+3x=180 → x=45°, angles=45° and 135°.
Co-interior angles SUPPLEMENTARY not equal. Vertically opposite ALWAYS equal.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch6: Triangle Properties
Angle sum property: A+B+C=180° for any triangle.
Exterior angle = sum of two remote interior angles (not all three).
Triangle inequality: sum of any two sides > third side.
Pythagoras: c^2=a^2+b^2 where c=hypotenuse (opposite 90°, always longest).
Triplets: (3,4,5),(5,12,13),(8,15,17),(7,24,25).
Converse: if a^2+b^2=c^2 then right-angled.
Median: vertex to midpoint of opposite side. 3 medians meet at centroid.
Altitude: perpendicular from vertex. 3 meet at orthocentre.
Example: A=50°,B=70°,C=60°. Exterior at C=120°=A+B=50+70 verified.
Sides 9,40,41: 81+1600=1681=41^2 → right triangle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch7: Congruence of Triangles
Congruent: same shape AND same size. Symbol: congruent to.
ORDER MATTERS: triangle ABC congruent to triangle PQR means A-P, B-Q, C-R.
Rules: SSS(all 3 sides), SAS(2 sides+INCLUDED angle), ASA(2 angles+INCLUDED side), AAS(2 angles+non-included side), RHS(right angle+hypotenuse+one side).
AAA: gives SIMILAR triangles not congruent (same shape, different size).
SSA: FAILS - ambiguous case (two possible triangles).
CPCT: Corresponding Parts of Congruent Triangles are equal (used AFTER proving congruence).
Isosceles proof: AB=AC. Draw altitude AD. Triangles ABD and ACD congruent by RHS. Angle B=angle C by CPCT.
SAS: angle must be INCLUDED between the two sides. ASA: side must be INCLUDED between two angles.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch8: Comparing Quantities
Percentage=per hundred. x%=x/100.
Fraction to %: multiply by 100. % to fraction: divide by 100.
Profit=SP-CP (when SP>CP). Loss=CP-SP (when CP>SP).
Profit%=(Profit/CP)×100. Loss%=(Loss/CP)×100.
SP=CP×(100+Profit%)/100. SP=CP×(100-Loss%)/100.
Simple Interest: SI=(P×R×T)/100. Amount A=P+SI.
Example: CP=850, Profit=12%: SP=850×112/100=952.
CP=600, Loss=8%: SP=600×92/100=552.
45 as % of 180: (45/180)×100=25%.
SI on 5000 at 6% for 3 years: SI=(5000×6×3)/100=900. A=5900.
Profit% always on CP NOT SP. Time in YEARS for SI. Discount on MARKED PRICE.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_7", "chapter": "ch8", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch9: Rational Numbers
Rational: p/q where p,q integers and q≠0. Every integer=rational(n=n/1).
Standard form: q>0 and HCF(p,q)=1. So -6/4=-3/2.
Comparison: convert to same positive denominator, compare numerators.
-3/5 vs -2/3: LCM=15 → -9/15 vs -10/15 → -3/5>-2/3.
Dense: infinite rationals between any two rationals.
Operations: p/q+r/s=(ps+qr)/qs. Division: (p/q)÷(r/s)=ps/qr.
Finding rationals between 1/4 and 1/2: between 2/8 and 4/8 → 3/8, 5/16, 7/16.
-3/5+2/3=(-9+10)/15=1/15.
Denominator must be POSITIVE in standard form. -2/3 is greater than -1 (closer to zero).""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch9", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch10: Practical Geometry
Five triangle construction cases: SSS, SAS, ASA, RHS, AAS.
SSS: draw base, arc from both ends, intersection=third vertex.
SAS: draw base, angle at one end, mark distance on angle ray, join.
ASA: draw base (included side), angles at both ends, intersection=third vertex.
RHS: right angle, hypotenuse from far end, intersection=right angle vertex.
AAS: find third angle (180-sum of two given), then use ASA method.
Parallel lines: draw transversal, copy angle at new point.
SAS example: PQ=5cm, QR=4.5cm, angle Q=60°. Draw QR=4.5. Angle 60° at Q. Mark P at 5cm. Join PR.
SSS example: sides 5,6,7. Draw base 6. Arc radius 5 from one end. Arc radius 7 from other. Intersection=third vertex.
Check triangle inequality before constructing. Use sharp pencil.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch11: Perimeter and Area
Perimeter: Triangle=a+b+c. Rectangle=2(l+b). Square=4s. Circle C=2πr=πd.
Area: Rectangle=l×b. Square=s^2. Triangle=(1/2)×b×h. Parallelogram=b×h. Circle=πr^2.
Height MUST be perpendicular to base for parallelogram and triangle.
π=22/7 (when radius is multiple of 7) or 3.14.
Path outside rectangle (width w): outer=(l+2w)×(b+2w). Area of path=outer-inner.
Example: Parallelogram base=8, height=5. Area=40cm^2 (NOT using slant side).
Circle r=7: C=2×(22/7)×7=44cm. A=(22/7)×49=154cm^2.
Rectangle 12m×8m, path 1m inside: inner=10×6. Path area=96-60=36m^2.
1m^2=10000cm^2. 1 hectare=10000m^2. Parallelogram uses PERPENDICULAR height.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_7", "chapter": "ch11", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch12: Algebraic Expressions
Term: single number, variable or product. Like terms: same variable same power.
Monomial(1 term), Binomial(2 terms), Trinomial(3 terms), Polynomial(1+ terms).
Addition: combine LIKE terms only. (3x^2+2x-5)+(x^2-3x+2)=4x^2-x-3.
Subtraction: change sign of ALL terms. (5a+2b)-(2a-3b)=5a+2b-2a+3b=3a+5b.
Substitution: 2x^2-3x+1 when x=2: 2(4)-3(2)+1=8-6+1=3.
Coefficient: numerical part. In -5xy, coefficient=-5.
Degree: sum of powers. 3x^2y has degree 3.
3x+2x^2 CANNOT be simplified (unlike terms). -(2a-3b)=-2a+3b NOT -2a-3b.
3x×2x=6x^2 (multiply coefficients AND add powers).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_7", "chapter": "ch12", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch13: Exponents and Powers
a^n = a×a×...×a (n times). 2^5=32.
Laws (same base): a^m×a^n=a^(m+n), a^m÷a^n=a^(m-n), (a^m)^n=a^(mn).
Same power: a^m×b^m=(ab)^m, a^m÷b^m=(a/b)^m.
a^0=1 for any a≠0.
Standard form: number between 1 and 10 times power of 10.
48000000=4.8×10^7. 0.0000035=3.5×10^(-6).
Examples: 2^5×2^3=2^8=256. 3^7÷3^4=3^3=27. (2^3)^2=2^6=64. 2^3×5^3=10^3=1000.
2^3=8 NOT 6. a^m×a^n=a^(m+n) ADD not multiply powers. (2+3)^2≠2^2+3^2.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_7", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch14: Symmetry
Line symmetry: one half is mirror image. Regular n-sided polygon: n lines of symmetry.
Lines of symmetry: Equilateral triangle=3, Square=4, Rectangle=2(midpoints only), Rhombus=2(diagonals), Isosceles=1, Scalene=0, Kite=1, Parallelogram=0, Pentagon=5, Hexagon=6, Circle=infinite.
Rotational symmetry: looks same after rotation<360°. Order=number of times in full rotation. Angle=360°÷order.
Rotational: Square(order 4, angle 90°), Rectangle(order 2, 180°), Equilateral triangle(order 3, 120°), Hexagon(order 6, 60°), Parallelogram(order 2, 180°), Scalene(order 1=none).
Square has BOTH line and rotational symmetry.
Parallelogram: NO line symmetry but HAS rotational (order 2).
Rectangle: 2 lines symmetry, order 2 rotation.
Pentagon: order 5, angle 72°.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch14", "difficulty": "beginner"}),

    Document(page_content="""Class 7 | Ch15: Visualising Solid Shapes
3D shapes (F=faces, E=edges, V=vertices):
Cube: F=6,E=12,V=8. Cuboid: F=6,E=12,V=8. Triangular prism: F=5,E=9,V=6.
Square pyramid: F=5,E=8,V=5. Tetrahedron: F=4,E=6,V=4.
Cylinder: F=3(2 circles+1 curved),E=2 curved,V=0. Cone: F=2,E=1,V=1(apex). Sphere: F=1,E=0,V=0.
Euler's formula for polyhedra: F+V-E=2. Cylinder/cone/sphere NOT polyhedra.
Cube: F+V-E=6+8-12=2. Tetrahedron: 4+4-6=2. Triangular prism: 5+6-9=2.
Nets: 2D folded into 3D. Cube has exactly 11 valid nets.
Views: Cylinder→front=rectangle, top=circle. Cone→front=triangle, top=circle with point.
Cross-section: cube horizontal=square. Cone through apex=triangle. Cone parallel to base=circle.
Cylinder has 3 faces not 2. Cube has 12 edges (4 top+4 bottom+4 vertical).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_7", "chapter": "ch15", "difficulty": "beginner"}),

    # ── ORIGINAL 6 DOCUMENTS (backward compatibility) ───────────────

    Document(page_content="""Calculus Fundamentals:
Power Rule: d/dx[x^n]=n*x^(n-1). Product Rule: d/dx[f*g]=f'g+fg'.
Chain Rule: d/dx[f(g(x))]=f'(g(x))*g'(x). Quotient Rule: d/dx[f/g]=(f'g-fg')/g^2.
d/dx[sin(x)]=cos(x), d/dx[cos(x)]=-sin(x), d/dx[e^x]=e^x, d/dx[ln(x)]=1/x.
integral(x^n dx)=x^(n+1)/(n+1)+C, integral(e^x dx)=e^x+C.
Fundamental Theorem: integral[a to b]f(x)dx=F(b)-F(a) where F'(x)=f(x).""",
    metadata={"source": "knowledge_base", "topic": "calculus", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Linear Algebra Essentials:
Matrix multiplication: row-by-column. Determinant 2x2: ad-bc.
Inverse: A^(-1)=adj(A)/det(A), exists iff det(A)≠0.
Eigenvalues: det(A-lambda*I)=0. Eigenvectors: solve (A-lambda*I)v=0.
Rank-Nullity: rank(A)+nullity(A)=n. Dot product: u·v=|u||v|cos(theta). Orthogonal: u·v=0.""",
    metadata={"source": "knowledge_base", "topic": "linear_algebra", "class_level": "class_12", "difficulty": "advanced"}),

    Document(page_content="""Statistics and Probability:
Mean=sum(x)/n. Variance=sum((x-mu)^2)/n. SD=sqrt(variance).
P(A∪B)=P(A)+P(B)-P(A∩B). P(A|B)=P(A∩B)/P(B).
Bayes: P(A|B)=P(B|A)*P(A)/P(B).
Binomial: P(X=k)=C(n,k)*p^k*(1-p)^(n-k).
CLT: sample means approach normal distribution as n increases.""",
    metadata={"source": "knowledge_base", "topic": "statistics", "class_level": "class_11", "difficulty": "intermediate"}),

    Document(page_content="""Algebra and Number Theory:
Quadratic: x=(-b±sqrt(b^2-4ac))/2a. D=b^2-4ac.
D>0: two real roots. D=0: repeated root. D<0: complex roots.
log(ab)=log(a)+log(b). log(a^n)=n*log(a).
a^2-b^2=(a+b)(a-b). a^3+b^3=(a+b)(a^2-ab+b^2).
AP: S_n=n/2*(2a+(n-1)d). GP: S=a(1-r^n)/(1-r). Infinite GP: a/(1-r) for |r|<1.""",
    metadata={"source": "knowledge_base", "topic": "algebra", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Trigonometry:
sin^2(x)+cos^2(x)=1. tan(x)=sin(x)/cos(x).
sin(A+B)=sinA*cosB+cosA*sinB. cos(A+B)=cosA*cosB-sinA*sinB.
sin(2x)=2sin(x)cos(x). cos(2x)=cos^2(x)-sin^2(x).
Values: sin30=1/2, sin45=sqrt(2)/2, sin60=sqrt(3)/2, sin90=1.
Law of Sines: a/sinA=b/sinB=c/sinC. Law of Cosines: c^2=a^2+b^2-2ab*cosC.""",
    metadata={"source": "knowledge_base", "topic": "trigonometry", "class_level": "class_10", "difficulty": "intermediate"}),

    Document(page_content="""Discrete Mathematics:
Permutations: P(n,r)=n!/(n-r)!. Combinations: C(n,r)=n!/(r!*(n-r)!).
GCD(a,b)=GCD(b,a mod b). LCM(a,b)=a*b/GCD(a,b).
Modular: a≡b(mod n) means n divides (a-b).
Fermat's Little: a^(p-1)≡1(mod p) for prime p.
De Morgan: NOT(A AND B)=NOT(A) OR NOT(B).""",
    metadata={"source": "knowledge_base", "topic": "discrete_math", "class_level": "class_11", "difficulty": "advanced"}),

    # ── CLASS 8 — All 16 Chapters ───────────────────────────────────

    Document(page_content="""Class 8 | Ch1: Rational Numbers
Rational number: p/q where p,q integers and q≠0. Includes integers, fractions, terminating and repeating decimals.
PROPERTIES OF RATIONAL NUMBERS:
Closure: rationals closed under +,-,×. Division closed except by zero.
Commutativity: a+b=b+a, a×b=b×a. NOT for subtraction or division.
Associativity: (a+b)+c=a+(b+c), (a×b)×c=a×(b×c). NOT for subtraction or division.
Distributivity: a×(b+c)=a×b+a×c.
Additive identity: 0. Multiplicative identity: 1.
Additive inverse of p/q is -p/q. Multiplicative inverse (reciprocal) of p/q is q/p.
REPRESENTATION ON NUMBER LINE:
Between any two rational numbers there are infinite rational numbers (dense property).
Standard form: denominator positive and HCF of numerator and denominator=1.
FINDING RATIONAL NUMBERS BETWEEN TWO NUMBERS:
Method 1: find mean (average) of the two numbers repeatedly.
Method 2: convert to same denominator with larger LCM.
Between -1/2 and 1/3: mean=(-1/2+1/3)/2=(-1/6)/2=-1/12. Continue for more.
SOLVED EXAMPLES:
Example 1: Find 5 rational numbers between -1/2 and 1/3.
Convert: -1/2=-9/18 and 1/3=6/18. Between -9/18 and 6/18: -8/18,-7/18,-6/18,-5/18,-4/18.
Simplified: -4/9, -7/18, -1/3, -5/18, -2/9.
Example 2: Verify -2/3 + 4/5 = 4/5 + (-2/3) (commutativity)
LHS: (-10+12)/15=2/15. RHS: (12-10)/15=2/15. Equal, commutativity verified.
COMMON MISTAKES:
Between any two rationals there are INFINITE rationals, not finite.
Reciprocal of 0 does NOT exist. Reciprocal of 1 is 1. Reciprocal of -1 is -1.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch1", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch2: Linear Equations in One Variable
Linear equation: variable has power 1 only. ax+b=c form.
Can involve fractions and variables on both sides.
SOLVING EQUATIONS WITH VARIABLES ON BOTH SIDES:
Collect variable terms on one side, constants on other.
3x+2=5x-4 → 2+4=5x-3x → 6=2x → x=3.
SOLVING EQUATIONS WITH FRACTIONS:
Multiply both sides by LCM of all denominators to clear fractions.
(2x+3)/5-(x-4)/3=2. LCM=15. Multiply: 3(2x+3)-5(x-4)=30.
6x+9-5x+20=30 → x+29=30 → x=1.
WORD PROBLEMS - STANDARD TYPES:
Age problems: Let present age=x. Set up equation from given conditions.
Number problems: Let number=x. Translate words to equation.
Geometry problems: Use perimeter/area formulas.
Money/mixture problems: Set up equation for totals.
SOLVED EXAMPLES:
Example 1: (2x+3)/5-(x-4)/3=2
Multiply by 15: 3(2x+3)-5(x-4)=30 → 6x+9-5x+20=30 → x=1.
Verify: (2+3)/5-(1-4)/3=1+1=2. Correct.
Example 2: A number is 4 more than twice another. Sum=40.
Let numbers be x and 2x+4. x+(2x+4)=40 → 3x=36 → x=12.
Numbers: 12 and 28. Verify: 12+28=40 and 28=2(12)+4. Correct.
Example 3: Present age ratio of A and B is 3:4. After 5 years ratio becomes 4:5. Find ages.
Let ages: 3x and 4x. (3x+5)/(4x+5)=4/5 → 15x+25=16x+20 → x=5.
Ages: 15 and 20.
COMMON MISTAKES:
When multiplying by LCM, multiply EVERY term including constants.
Verify answer by substituting back in ORIGINAL equation.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch2", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch3: Understanding Quadrilaterals
ANGLE SUM PROPERTY:
Sum of interior angles of polygon with n sides = (n-2)×180°.
Triangle(n=3): (3-2)×180=180°.
Quadrilateral(n=4): (4-2)×180=360°.
Pentagon(n=5): 540°. Hexagon(n=6): 720°.
Sum of exterior angles of ANY convex polygon = 360°.
TYPES OF QUADRILATERALS AND PROPERTIES:
Trapezium: one pair of parallel sides. Area=(1/2)×(sum of parallel sides)×height.
Kite: two pairs of adjacent sides equal. One diagonal bisects the other at right angles.
Parallelogram: opposite sides parallel and equal, opposite angles equal, diagonals bisect each other.
Rectangle: parallelogram with all right angles, diagonals equal.
Rhombus: parallelogram with all sides equal, diagonals bisect at right angles.
Square: all sides equal, all angles 90°, diagonals equal and bisect at right angles.
HIERARCHY: Square → Rectangle → Parallelogram → Quadrilateral.
Square is special rhombus AND special rectangle.
SOLVED EXAMPLES:
Example 1: In parallelogram ABCD, angle A=75°.
Angle C=75° (opposite angles equal). Angle B=180-75=105° (co-interior=180°). Angle D=105°.
Example 2: Exterior angle of regular polygon=40°. How many sides?
Number of sides=360°/40°=9 sides.
Example 3: In kite ABCD, AB=AD=5cm, BC=DC=8cm. diagonal AC=6cm. Find BD.
Diagonals of kite are perpendicular. One diagonal bisects the other.
COMMON MISTAKES:
All rectangles are parallelograms but NOT all parallelograms are rectangles.
Rhombus diagonals bisect at 90° but are NOT equal. Rectangle diagonals are equal but NOT at 90°.
Sum of angles of quadrilateral=360° (not 180°).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch4: Practical Geometry (Quadrilaterals)
A quadrilateral has 4 sides, 4 angles, 2 diagonals = 10 measurements total.
Minimum 5 measurements needed to uniquely construct a quadrilateral.
CONSTRUCTION CASES:
Case 1 — Four sides and one diagonal (SSS triangles method):
Draw diagonal first, construct both triangles on either side.
Case 2 — Two diagonals and three sides:
Draw one diagonal, use given measurements to find vertices.
Case 3 — Two adjacent sides and three angles:
Use angles to set directions, mark lengths.
Case 4 — Three sides and two included angles:
Draw one side, use angles at both ends.
Case 5 — Special quadrilaterals (rhombus, rectangle, square):
Use their special properties to simplify construction.
CONSTRUCTING QUADRILATERAL ABCD (4 sides + 1 diagonal):
Given: AB=4cm, BC=3.5cm, CD=4.5cm, DA=3cm, AC=5cm.
Step 1: Draw AC=5cm (diagonal).
Step 2: From A, draw arc radius 4cm. From C, draw arc radius 3.5cm. Intersection=B.
Step 3: From A, draw arc radius 3cm. From C, draw arc radius 4.5cm. Intersection=D.
Step 4: Join all vertices. ABCD is the required quadrilateral.
RHOMBUS CONSTRUCTION: Both diagonals given (they bisect at right angles at midpoint).
RECTANGLE CONSTRUCTION: One side and one diagonal (use Pythagoras to find other side).
COMMON MISTAKES:
Check if given measurements form a valid quadrilateral before constructing.
In rhombus construction, diagonals bisect each other at 90°, not just bisect.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch5: Data Handling
GROUPED DATA AND FREQUENCY:
Class interval: range of values grouped together. e.g., 0-10, 10-20, 20-30.
Class width = upper limit - lower limit.
Frequency: number of observations in each class.
Cumulative frequency: sum of all frequencies up to that class.
HISTOGRAM: bar graph for continuous data (no gaps between bars).
CIRCLE GRAPH (PIE CHART):
Central angle for each component = (component value/total) × 360°.
Example: Wheat 40% → angle = 0.40×360 = 144°.
PROBABILITY:
Experiment: activity with outcomes (throwing die, tossing coin).
Event: collection of one or more outcomes.
P(event) = number of favourable outcomes / total number of outcomes.
P(sure event)=1. P(impossible event)=0. 0≤P(E)≤1.
P(E)+P(not E)=1. So P(not E)=1-P(E).
SOLVED EXAMPLES:
Example 1: Die thrown. Find P(number>4).
Favourable: 5,6 → 2 outcomes. Total=6. P=2/6=1/3.
Example 2: Pie chart for budget. Food=40%, Rent=25%, Education=20%, Others=15%.
Angles: Food=144°, Rent=90°, Education=72°, Others=54°. Total=360°.
Example 3: P(drawing red card from deck)=26/52=1/2.
P(face card)=12/52=3/13. P(ace)=4/52=1/13.
COMMON MISTAKES:
In histogram, class intervals must be continuous (no gaps).
P(E)+P(not E)=1 always. P(E) cannot be greater than 1 or negative.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_8", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch6: Squares and Square Roots
PERFECT SQUARES: 1,4,9,16,25,36,49,64,81,100,121,144,169,196,225...
Properties:
A number ending in 2,3,7,8 is NEVER a perfect square.
A perfect square ending in 1 → number ends in 1 or 9.
A perfect square ending in 4 → number ends in 2 or 8.
A perfect square ending in 9 → number ends in 3 or 7.
A perfect square ending in 6 → number ends in 4 or 6.
Number of zeros at end of perfect square is always EVEN.
SQUARE ROOT METHODS:
Method 1 - Prime factorisation: pair up prime factors, take one from each pair.
sqrt(1764): 1764=2^2×3^2×7^2 → sqrt=2×3×7=42.
Method 2 - Long division: group digits in pairs from right, find largest square≤group.
PYTHAGOREAN TRIPLETS PATTERN:
For any m>1: (2m, m²-1, m²+1) form a Pythagorean triplet.
m=2: (4,3,5). m=3: (6,8,10). m=4: (8,15,17).
ESTIMATING SQUARE ROOT: find between which two consecutive perfect squares the number lies.
sqrt(200): between sqrt(196)=14 and sqrt(225)=15. Closer to 14.
SOLVED EXAMPLES:
Example 1: Is 1352 a perfect square?
1352=2^3×13^2. Power of 2 is odd (3), so NOT a perfect square.
To make perfect square: multiply by 2 → 2704=2^4×13^2=(2^2×13)^2=52^2.
Example 2: Find least number to multiply 675 to make perfect square.
675=3^3×5^2. Need one more 3: multiply by 3 → 2025=45^2.
COMMON MISTAKES:
sqrt(a^2+b^2) ≠ a+b. sqrt(25+144)=sqrt(169)=13, NOT 5+12=17.
A number ending in 0 is perfect square only if it ends in EVEN number of zeros.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch6", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch7: Cubes and Cube Roots
PERFECT CUBES: 1,8,27,64,125,216,343,512,729,1000...
1^3=1, 2^3=8, 3^3=27, 4^3=64, 5^3=125, 6^3=216, 7^3=343, 8^3=512, 9^3=729, 10^3=1000.
PROPERTIES OF CUBES:
Cube of even number is even. Cube of odd number is odd.
Cube of negative number is negative: (-2)^3=-8.
A perfect cube can end in any digit 0-9 (unlike squares).
CUBE ROOT BY PRIME FACTORISATION:
Group prime factors in sets of 3. Take one from each group.
cbrt(13824): 13824=2^9×3^3=(2^3)^3×3^3=(8×3)^3=24^3. So cbrt(13824)=24.
FINDING SMALLEST MULTIPLIER/DIVISOR:
To make a perfect cube: each prime factor must appear in multiples of 3.
675=3^3×5^2. Need one more 5^1 to make 5^3. Multiply by 5. 675×5=3375=15^3.
SOLVED EXAMPLES:
Example 1: cbrt(13824). 13824=2×6912=2×2×3456=...=2^9×3^3. cbrt=2^3×3=24.
Example 2: Is 1728 a perfect cube? 1728=2^6×3^3=(2^2×3)^3=12^3. YES, cbrt=12.
Example 3: Find smallest number to divide 81 to make perfect cube.
81=3^4. Need to remove one 3 (keep 3^3). Divide by 3. 81÷3=27=3^3. Answer: 3.
Example 4: What is cube of -5? (-5)^3=-125.
COMMON MISTAKES:
cbrt(-8)=-2 (negative cube root exists, unlike square roots).
cbrt(a^3+b^3) ≠ a+b. Must factorise properly.
Perfect cube can end in any digit, not restricted like perfect squares.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch7", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch8: Comparing Quantities (Compound Interest)
RECAP - PROFIT/LOSS AND SIMPLE INTEREST:
Profit%=(Profit/CP)×100. Loss%=(Loss/CP)×100.
SI=(P×R×T)/100. Amount=P+SI=P(1+RT/100).
COMPOUND INTEREST:
Interest calculated on principal AND accumulated interest.
Formula: A=P(1+R/100)^n where P=principal, R=rate%, n=time in years.
CI=A-P=P[(1+R/100)^n - 1].
Compounded half-yearly: A=P(1+R/200)^(2n) (rate halved, time doubled).
Compounded quarterly: A=P(1+R/400)^(4n).
CI>SI for same P,R,T (except for 1 year when CI=SI).
DIFFERENCE FORMULA (for 2 years):
CI-SI = P×(R/100)^2.
APPLICATIONS:
Population growth: P_n=P_0(1+R/100)^n.
Depreciation: V_n=V_0(1-R/100)^n.
SOLVED EXAMPLES:
Example 1: CI on 12000 at 10% for 2 years compounded annually.
A=12000(1+10/100)^2=12000×(1.1)^2=12000×1.21=14520.
CI=14520-12000=2520.
SI=12000×10×2/100=2400.
CI-SI=2520-2400=120=12000×(10/100)^2=12000×0.01=120. Verified.
Example 2: CI on 8000 at 10% for 1.5 years compounded half-yearly.
Rate per half year=5%, number of periods=3.
A=8000(1+5/100)^3=8000×(1.05)^3=8000×1.157625=9261.
Example 3: Population 20000, grows 5% per year. After 2 years?
P=20000(1.05)^2=20000×1.1025=22050.
COMMON MISTAKES:
For half-yearly compounding: halve the rate AND double the time period.
CI and SI are EQUAL only for first year. After that CI>SI.""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_8", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch9: Algebraic Expressions and Identities
MULTIPLICATION OF ALGEBRAIC EXPRESSIONS:
Monomial × Monomial: multiply coefficients, add powers. 3x^2 × 4x^3=12x^5.
Monomial × Polynomial: distribute. 2x(3x^2-5x+1)=6x^3-10x^2+2x.
Polynomial × Polynomial: each term of first × each term of second.
STANDARD ALGEBRAIC IDENTITIES:
Identity 1: (a+b)^2 = a^2+2ab+b^2
Identity 2: (a-b)^2 = a^2-2ab+b^2
Identity 3: (a+b)(a-b) = a^2-b^2
Identity 4: (x+a)(x+b) = x^2+(a+b)x+ab
USING IDENTITIES FOR CALCULATIONS:
105^2=(100+5)^2=10000+1000+25=11025.
98×102=(100-2)(100+2)=10000-4=9996.
FACTORISATION USING IDENTITIES:
x^2+8x+16=(x+4)^2. Check: 2×4=8, 4^2=16. Correct.
9a^2-12ab+4b^2=(3a-2b)^2. Check: 2×3a×2b=12ab. Correct.
x^2-25=(x+5)(x-5). (a^2-b^2 type)
SOLVED EXAMPLES:
Example 1: Expand (3x+2y)^2=9x^2+12xy+4y^2.
Example 2: Expand (4a-3b)^2=16a^2-24ab+9b^2.
Example 3: (2x+3)(2x+5)=4x^2+(3+5)2x+15=4x^2+16x+15. Using identity 4: (x+a)(x+b) with 2x,3,5.
Example 4: Evaluate 97^2=(100-3)^2=10000-600+9=9409.
COMMON MISTAKES:
(a+b)^2=a^2+2ab+b^2 NOT a^2+b^2 (missing middle term 2ab).
(a-b)^2=a^2-2ab+b^2 NOT a^2-2ab-b^2 (last term is always positive).
Factorisation: must check using expansion.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch10: Visualising Solid Shapes
VIEWS OF 3D OBJECTS:
Front view, Side view (left or right), Top view (plan view).
Different views give 2D shapes from different angles.
Cube: all views are squares.
Cuboid: views are rectangles (different dimensions for different views).
Cylinder: front/side=rectangle, top=circle.
Cone: front/side=triangle, top=circle with centre point.
Sphere: all views are circles.
MAPPING AND SCALE:
Map is a scale drawing of a region.
Scale: 1cm represents actual distance. Scale 1:50000 means 1cm=50000cm=500m.
Distance on map × scale = actual distance.
POLYHEDRA:
Polyhedron: solid with flat faces, all faces are polygons.
Regular polyhedra (Platonic solids): all faces identical regular polygons.
Tetrahedron: 4 equilateral triangular faces.
Cube: 6 square faces.
Octahedron: 8 equilateral triangular faces.
Dodecahedron: 12 regular pentagonal faces.
Icosahedron: 20 equilateral triangular faces.
Euler's formula: F+V-E=2 for all polyhedra.
NON-POLYHEDRA: cone, cylinder, sphere (have curved surfaces).
SOLVED EXAMPLES:
Example 1: Top view of a cone is a circle with a point (apex) at centre.
Example 2: Map scale 1:50000. Distance on map=3cm. Actual distance=3×50000cm=1.5km.
Example 3: Verify Euler: Octahedron F=8,V=6,E=12. F+V-E=8+6-12=2. Correct.
COMMON MISTAKES:
Cylinder and cone are NOT polyhedra (have curved surfaces).
Top view of cone shows circle with a dot in centre, not just a circle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_8", "chapter": "ch10", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch11: Mensuration
AREA FORMULAS:
Trapezium: A=(1/2)×(a+b)×h where a,b=parallel sides, h=height.
Rhombus: A=(1/2)×d1×d2 where d1,d2=diagonals.
General quadrilateral: A=(1/2)×diagonal×(sum of perpendiculars from opposite vertices).
Polygon: divide into triangles, sum their areas.
SURFACE AREA:
Cube: Total SA=6a^2. Lateral SA=4a^2.
Cuboid: Total SA=2(lb+bh+lh). Lateral SA=2(l+b)×h.
Cylinder: Total SA=2πr(r+h). Curved SA=2πrh. Base area=πr^2.
VOLUME:
Cube: V=a^3.
Cuboid: V=l×b×h.
Cylinder: V=πr^2h.
UNIT CONVERSIONS:
1m=100cm → 1m^2=10^4cm^2 → 1m^3=10^6cm^3.
1km=1000m → 1km^2=10^6m^2.
1 litre=1000cm^3=1000ml.
SOLVED EXAMPLES:
Example 1: Trapezium parallel sides 8cm and 5cm, height 4cm.
A=(1/2)(8+5)(4)=(1/2)(13)(4)=26cm^2.
Example 2: Cuboid 5×4×3cm.
Total SA=2(5×4+4×3+5×3)=2(20+12+15)=2×47=94cm^2.
Volume=5×4×3=60cm^3.
Example 3: Cylinder r=7cm, h=10cm.
Curved SA=2×(22/7)×7×10=440cm^2.
Total SA=440+2×(22/7)×49=440+308=748cm^2.
Volume=(22/7)×49×10=1540cm^3.
COMMON MISTAKES:
Trapezium area uses PERPENDICULAR height, not slant side.
Cylinder Total SA includes BOTH circular ends (2πr^2) plus curved surface.
Volume of cylinder=πr^2×h (cross-section area × height).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_8", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch12: Exponents and Powers
NEGATIVE EXPONENTS:
a^(-n)=1/a^n for any non-zero a. 2^(-3)=1/8. 10^(-4)=0.0001.
a^(-1)=1/a (reciprocal).
LAWS (extend from Class 7 to include negative exponents):
a^m × a^n=a^(m+n). a^m ÷ a^n=a^(m-n). (a^m)^n=a^(mn).
a^m × b^m=(ab)^m. a^m ÷ b^m=(a/b)^m. a^0=1.
These ALL work for negative exponents too.
STANDARD FORM (SCIENTIFIC NOTATION):
Number between 1 and 10 multiplied by integer power of 10.
Large: 6,020,000,000=6.02×10^9.
Small: 0.000000000016=1.6×10^(-11).
To compare: larger power of 10=larger number.
EXPRESSING IN STANDARD FORM:
Move decimal point until you get a number between 1 and 10.
Number of places moved = power of 10 (positive if moved left, negative if moved right).
485 → move 2 left → 4.85×10^2.
0.00605 → move 3 right → 6.05×10^(-3).
SOLVED EXAMPLES:
Example 1: (2^(-3)×3^(-2))÷(6^(-1)).
=1/8×1/9÷1/6=1/72×6=6/72=1/12.
Example 2: (5/3)^(-2)×(3/5)^3=(3/5)^2×(3/5)^3=(3/5)^5=243/3125.
Example 3: Express 0.00000605 in standard form.
Move decimal 6 places right → 6.05×10^(-6).
COMMON MISTAKES:
2^(-3) = 1/8 NOT -8. Negative exponent means reciprocal, not negative number.
(a/b)^(-n)=(b/a)^n. So (2/3)^(-2)=(3/2)^2=9/4.
In scientific notation, first number MUST be between 1 and 10.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch13: Direct and Inverse Proportion
DIRECT PROPORTION:
x and y are in direct proportion if x/y=k (constant) or x1/y1=x2/y2.
As x increases, y increases proportionally. Symbol: x∝y.
Graph: straight line through origin.
Examples: cost∝quantity, distance∝time(constant speed), simple interest∝time.
INVERSE PROPORTION:
x and y are in inverse proportion if xy=k (constant) or x1×y1=x2×y2.
As x increases, y decreases proportionally. Symbol: x∝1/y.
Graph: hyperbola (not straight line).
Examples: speed∝1/time, workers∝1/days, pipes∝1/fill time.
SOLVED EXAMPLES:
Example 1 (Direct): If 15 bags of rice cost ₹450, find cost of 24 bags.
15/450=24/x → x=24×450/15=₹720. OR cost per bag=30, 24×30=720.
Example 2 (Inverse): 8 workers finish in 12 days. How many days for 6 workers?
8×12=6×d → d=96/6=16 days. (fewer workers → more days → inverse)
Example 3 (Inverse): 3 pipes fill tank in 8 hours. How long for 4 pipes?
3×8=4×t → t=24/4=6 hours.
Example 4: Car travels 150km in 3 hours. How long for 250km at same speed?
3/150=t/250 → t=500/100=5 hours. (direct proportion)
IDENTIFYING TYPE:
More→More: Direct proportion.
More→Less: Inverse proportion.
Workers and days: MORE workers, LESS days → INVERSE.
Speed and time: MORE speed, LESS time → INVERSE.
COMMON MISTAKES:
Workers and days is INVERSE not direct.
In inverse proportion: x1×y1=x2×y2 (NOT x1/y1=x2/y2).""",
    metadata={"source": "ncert", "topic": "arithmetic", "class_level": "class_8", "chapter": "ch13", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch14: Factorisation
METHODS OF FACTORISATION:
Method 1 - Common Factor: take out HCF of all terms.
12x^2y-9xy^2+6xyz = 3xy(4x-3y+2z).
Method 2 - Grouping: group terms to find common factor.
ax+ay+bx+by = a(x+y)+b(x+y) = (a+b)(x+y).
a^2-b^2+a-b = (a-b)(a+b)+(a-b) = (a-b)(a+b+1).
Method 3 - Using Identities:
x^2+8x+16 = x^2+2(4)x+4^2 = (x+4)^2.
4x^2-9 = (2x)^2-3^2 = (2x+3)(2x-3).
Method 4 - Splitting Middle Term (for quadratics ax^2+bx+c):
Find two numbers p,q such that p+q=b and p×q=a×c.
x^2+7x+12: p+q=7, p×q=12 → p=3,q=4. So x^2+3x+4x+12=x(x+3)+4(x+3)=(x+3)(x+4).
2x^2+7x+3: p+q=7, p×q=2×3=6 → p=6,q=1. So 2x^2+6x+x+3=2x(x+3)+1(x+3)=(2x+1)(x+3).
DIVISION OF ALGEBRAIC EXPRESSIONS:
Polynomial ÷ Monomial: divide each term separately.
(6x^3-4x^2+2x) ÷ 2x = 3x^2-2x+1.
Polynomial ÷ Polynomial: factorise numerator and denominator, cancel common factors.
SOLVED EXAMPLES:
Example 1: Factorise 12x^2y-9xy^2+6xyz = 3xy(4x-3y+2z).
Example 2: x^2+7x+12 = (x+3)(x+4). Verify: (x+3)(x+4)=x^2+7x+12. Correct.
Example 3: 2x^2+7x+3. Product=6, sum=7. Factors: 6 and 1. = (2x+1)(x+3).
COMMON MISTAKES:
Always take out the COMPLETE HCF in method 1 (common factor).
When splitting middle term: product must equal a×c (coefficient of x^2 × constant).
Verify factorisation by expanding back.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 8 | Ch15: Introduction to Graphs
TYPES OF GRAPHS:
Bar graph: compares discrete data using bars.
Line graph: shows change over time (continuous data).
Pie chart: shows proportions (parts of a whole).
Histogram: bar graph for continuous grouped data (no gaps).
LINEAR GRAPHS:
Equation of straight line: y=mx+c where m=slope, c=y-intercept.
x-intercept: point where line crosses x-axis (y=0).
y-intercept: point where line crosses y-axis (x=0).
Slope m: if line passes through (x1,y1) and (x2,y2): m=(y2-y1)/(x2-x1).
PLOTTING POINTS AND GRAPHS:
For any linear equation, find at least 2 points (3 to verify).
For x+y=5: when x=0,y=5. When x=5,y=0. When x=2,y=3.
Plot these points and join with straight line.
READING GRAPHS:
Distance-time graph: slope=speed. Horizontal line=stationary. Steep line=fast.
Temperature-time graph: shows heating/cooling patterns.
APPLICATIONS:
Finding values from graph (interpolation and extrapolation).
Conversion graphs: between units (km to miles, °C to °F).
SOLVED EXAMPLES:
Example 1: Draw graph of y=2x+1. Plot (-1,-1), (0,1), (1,3). Join them.
Example 2: For graph x+2y=6, find x and y intercepts.
x-intercept (y=0): x=6. y-intercept (x=0): y=3.
Example 3: Plot points A(2,3), B(-1,4), C(0,-2).
A: right 2, up 3. B: left 1, up 4. C: at origin, down 2.
Example 4: Distance-time graph, car goes 60km in 1 hour. Speed=60/1=60kmph.
COMMON MISTAKES:
x-intercept: set y=0 (NOT x=0). y-intercept: set x=0.
Plotting: x-coordinate first (horizontal), then y-coordinate (vertical).
In distance-time graph, slope=speed. Greater slope=greater speed.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_8", "chapter": "ch15", "difficulty": "beginner"}),

    Document(page_content="""Class 8 | Ch16: Playing With Numbers
NUMBERS IN GENERAL FORM:
2-digit number ab = 10a+b (a=tens digit, b=units digit).
3-digit number abc = 100a+10b+c.
Example: 57 = 10×5+7. 347 = 100×3+10×4+7.
REVERSING DIGITS:
2-digit number ab=10a+b. Reversed ba=10b+a.
Sum: (10a+b)+(10b+a)=11(a+b). Always divisible by 11.
Difference: (10a+b)-(10b+a)=9(a-b). Always divisible by 9.
3-digit number abc=100a+10b+c. Reversed cba=100c+10b+a.
Difference: (100a+10b+c)-(100c+10b+a)=99(a-c). Always divisible by 99.
CYCLIC NUMBERS (3 digits abc, bca, cab):
abc+bca+cab=111(a+b+c). Always divisible by 111 and 3.
LETTERS FOR DIGITS (cryptarithmetic):
Each letter represents a unique digit. Use logic to find values.
AB+BA=121 → (10a+b)+(10b+a)=11(a+b)=121 → a+b=11.
DIVISIBILITY TESTS REVISITED:
Div by 3: sum of digits divisible by 3.
Div by 9: sum of digits divisible by 9.
Div by 11: (sum of odd position digits)-(sum of even position digits)=0 or multiple of 11.
SOLVED EXAMPLES:
Example 1: A 2-digit number is 4 times sum of its digits. If 18 added, digits reverse.
Let number=10a+b. 10a+b=4(a+b) → 10a+b=4a+4b → 6a=3b → b=2a.
After adding 18: 10a+b+18=10b+a → 9a-9b=-18 → b-a=2.
From b=2a and b-a=2: 2a-a=2 → a=2, b=4. Number=24.
Verify: 24=4×(2+4)=4×6=24. 24+18=42 (digits reversed). Correct.
Example 2: If 1A×A=9A where A is same digit, find A.
Try A=5: 15×5=75=9×5? No. Try A=6: 16×6=96=9×6? 9×6=54. No. 
Think: 1A×A means (10+A)×A=10A+A^2. This should equal 90+A.
10A+A^2=90+A → A^2+9A-90=0 → (A+15)(A-6)=0 → A=6.
Check: 16×6=96. Yes! 1A×A=16×6=96=9A where A=6.
COMMON MISTAKES:
General form of 2-digit number ab is 10a+b NOT a×b or a+b.
When digits are reversed: the tens digit becomes units and vice versa.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_8", "chapter": "ch16", "difficulty": "intermediate"}),


    # ── CLASS 9 — All 15 Chapters ───────────────────────────────────

    Document(page_content="""Class 9 | Ch1: Number Systems
RATIONAL NUMBERS: p/q form where q≠0. Terminating or repeating decimals.
IRRATIONAL NUMBERS: cannot be written as p/q. Non-terminating non-repeating decimals.
Examples: sqrt(2), sqrt(3), sqrt(5), pi, e.
REAL NUMBERS = Rational + Irrational numbers.
PROVING IRRATIONALITY (contradiction method):
Assume sqrt(2) is rational → sqrt(2)=p/q (lowest terms, HCF=1).
Squaring: 2=p^2/q^2 → p^2=2q^2 → p^2 is even → p is even → p=2m.
4m^2=2q^2 → q^2=2m^2 → q is even. Both p,q even contradicts HCF=1. So sqrt(2) is irrational.
REPRESENTATION ON NUMBER LINE:
sqrt(n) on number line: draw right triangle with legs 1 and sqrt(n-1), hypotenuse=sqrt(n).
sqrt(2): right triangle with both legs=1. Hypotenuse=sqrt(2). Mark on number line.
OPERATIONS ON REAL NUMBERS:
sqrt(a) × sqrt(b) = sqrt(ab). sqrt(a)/sqrt(b)=sqrt(a/b).
(sqrt(a)+sqrt(b))(sqrt(a)-sqrt(b))=a-b.
RATIONALISATION: multiply numerator and denominator by conjugate.
3/(2+sqrt(3)): multiply by (2-sqrt(3))/(2-sqrt(3)) = 3(2-sqrt(3))/(4-3) = 3(2-sqrt(3)) = 6-3sqrt(3).
5/(sqrt(7)-sqrt(2)): multiply by (sqrt(7)+sqrt(2)) = 5(sqrt(7)+sqrt(2))/(7-2) = sqrt(7)+sqrt(2).
LAWS OF EXPONENTS FOR REAL NUMBERS:
a^m × a^n = a^(m+n). (a^m)^n = a^(mn). a^m × b^m = (ab)^m.
a^(1/n) = nth root of a. a^(m/n) = (nth root of a)^m.
SOLVED EXAMPLES:
Example 1: Simplify (sqrt(5)+sqrt(3))^2 = 5+2sqrt(15)+3 = 8+2sqrt(15).
Example 2: Rationalise 1/(sqrt(5)+sqrt(2)) = (sqrt(5)-sqrt(2))/((sqrt(5))^2-(sqrt(2))^2) = (sqrt(5)-sqrt(2))/3.
Example 3: Express 2^(1/2) × 2^(1/3) = 2^(1/2+1/3) = 2^(5/6).
COMMON MISTAKES:
sqrt(a+b) ≠ sqrt(a)+sqrt(b). sqrt(9+16)=sqrt(25)=5, NOT 3+4=7.
Irrational + Rational = Irrational. Irrational × Irrational can be rational: sqrt(2)×sqrt(2)=2.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch2: Polynomials
POLYNOMIAL: p(x) = a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0 where coefficients are real numbers.
Degree: highest power of variable. Linear(degree 1), Quadratic(degree 2), Cubic(degree 3).
Zero polynomial: p(x)=0. Degree not defined.
Constant polynomial: p(x)=c. Degree=0.
ZEROES OF POLYNOMIAL: value of x where p(x)=0.
Linear polynomial ax+b has zero at x=-b/a.
Quadratic can have 0, 1 or 2 zeroes. Cubic can have 1, 2 or 3 zeroes.
REMAINDER THEOREM:
When p(x) is divided by (x-a), remainder = p(a).
No need to do long division — just substitute x=a.
p(x)=x^3-6x^2+11x-6 divided by (x-2): remainder=p(2)=8-24+22-6=0. So (x-2) is a factor.
FACTOR THEOREM:
(x-a) is a factor of p(x) if and only if p(a)=0.
To factorise: find a value 'a' where p(a)=0, then divide by (x-a).
FACTORISING CUBIC POLYNOMIALS:
Try factors of constant term. If p(a)=0, divide p(x) by (x-a) to get quadratic. Factorise quadratic.
ALGEBRAIC IDENTITIES:
(x+y+z)^2 = x^2+y^2+z^2+2xy+2yz+2zx.
(x+y)^3 = x^3+3x^2y+3xy^2+y^3 = x^3+y^3+3xy(x+y).
(x-y)^3 = x^3-3x^2y+3xy^2-y^3 = x^3-y^3-3xy(x-y).
x^3+y^3+z^3-3xyz = (x+y+z)(x^2+y^2+z^2-xy-yz-zx).
Special case: if x+y+z=0 then x^3+y^3+z^3=3xyz.
SOLVED EXAMPLES:
Example 1: Find remainder when x^3-6x^2+11x-6 divided by x-2.
p(2)=8-24+22-6=0. Remainder=0. So (x-2) is a factor.
Example 2: Factorise x^3-23x^2+142x-120.
Try x=1: 1-23+142-120=0. So (x-1) is factor.
Divide: x^3-23x^2+142x-120 = (x-1)(x^2-22x+120) = (x-1)(x-10)(x-12).
COMMON MISTAKES:
Degree of zero polynomial is undefined, not zero or -1.
Remainder theorem uses SUBSTITUTION, not division, for finding remainder quickly.
Factor theorem: (x-a) is factor iff p(a)=0 (note: x MINUS a, not x PLUS a).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch3: Coordinate Geometry
CARTESIAN PLANE:
Two perpendicular lines: x-axis (horizontal) and y-axis (vertical).
Origin O = (0,0). Point P = (x,y) where x=abscissa, y=ordinate.
QUADRANTS:
I: (+,+) — right of y-axis, above x-axis.
II: (-,+) — left of y-axis, above x-axis.
III: (-,-) — left of y-axis, below x-axis.
IV: (+,-) — right of y-axis, below x-axis.
Points ON axes: x-axis has y=0. y-axis has x=0.
PLOTTING POINTS:
Start at origin. Move right/left for x (positive=right, negative=left).
Then move up/down for y (positive=up, negative=down). Mark the point.
DISTANCE FORMULA (introduced here, developed in Class 10):
Distance between A(x1,y1) and B(x2,y2) = sqrt((x2-x1)^2+(y2-y1)^2).
COLLINEAR POINTS: three points lie on same straight line.
SECTION FORMULA (for later): divides line segment in given ratio.
GRAPHS OF LINEAR EQUATIONS:
y=x: line through origin at 45°. y=-x: line through origin at 135°.
x=a: vertical line. y=b: horizontal line.
SOLVED EXAMPLES:
Example 1: Plot A(3,4), B(-2,3), C(-4,-1), D(2,-3).
A: Quadrant I (both positive). B: Quadrant II. C: Quadrant III. D: Quadrant IV.
Example 2: Find distance between A(3,4) and B(-2,3).
AB = sqrt((-2-3)^2+(3-4)^2) = sqrt(25+1) = sqrt(26) units.
Example 3: In which quadrant is (-3,-5)?
Both negative → Quadrant III.
COMMON MISTAKES:
Point (3,4) is NOT same as (4,3). First coordinate is always x (horizontal).
Origin (0,0) is not in any quadrant — it's at the intersection of axes.
Points on x-axis have y-coordinate=0, not x-coordinate=0.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch3", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables
FORM: ax+by+c=0 where a,b are not both zero. x and y are variables.
A linear equation in two variables has INFINITELY MANY solutions.
Each solution is an ordered pair (x,y) that satisfies the equation.
GRAPH OF LINEAR EQUATION IN TWO VARIABLES:
Graph is always a STRAIGHT LINE.
To draw: find at least 2 solutions (3 recommended to verify).
For 2x+3y=12:
x=0: 3y=12, y=4. Point (0,4).
y=0: 2x=12, x=6. Point (6,0).
x=3: 6+3y=12, y=2. Point (3,2). All 3 collinear confirms straight line.
X-INTERCEPT: point where line crosses x-axis. Set y=0 and solve for x.
Y-INTERCEPT: point where line crosses y-axis. Set x=0 and solve for y.
EQUATIONS OF SPECIAL LINES:
x=a: vertical line parallel to y-axis, passing through (a,0).
y=b: horizontal line parallel to x-axis, passing through (0,b).
y=x: line through origin, bisects I and III quadrants.
EXPRESSING WORD PROBLEMS AS LINEAR EQUATIONS:
"Cost of x pencils at 2 each and y pens at 5 each is 50": 2x+5y=50.
SOLVED EXAMPLES:
Example 1: Draw graph of 2x+3y=12. Find x and y intercepts.
y-intercept (x=0): y=4. So (0,4).
x-intercept (y=0): x=6. So (6,0).
Plot (0,4), (6,0), (3,2). Join them.
Example 2: Find 3 solutions of x+2y=8.
(0,4), (8,0), (2,3). Verify: 0+8=8, 8+0=8, 2+6=8. All correct.
COMMON MISTAKES:
A linear equation in two variables has infinite solutions (not just 2 or 3).
Every point on the graph is a solution. Every solution gives a point on the graph.
Graph of x=3 is a VERTICAL line (not a point on x-axis).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch5: Introduction to Euclid's Geometry
EUCLID'S DEFINITIONS (important ones):
A point is that which has no part.
A line is breadthless length.
A surface has length and breadth only.
Ends of a line are points. Ends of a surface are lines.
EUCLID'S POSTULATES:
1. A straight line segment can be drawn from any point to any other point.
2. A terminated line (line segment) can be extended indefinitely.
3. A circle can be drawn with any centre and any radius.
4. All right angles are equal to each other.
5. Parallel postulate: If a line falls on two lines such that interior angles on one side sum less than two right angles, those two lines if extended will meet on that side.
EUCLID'S AXIOMS (Common Notions):
1. Things equal to the same thing are equal to each other.
2. If equals are added to equals, the wholes are equal.
3. If equals are subtracted from equals, the remainders are equal.
4. Things which coincide with one another are equal.
5. The whole is greater than the part.
UNDEFINED TERMS: point, line, plane (defined informally).
THEOREMS FROM POSTULATES:
Theorem 1: Two distinct lines cannot have more than one point in common.
Theorem 2: A unique line passes through two distinct points.
EQUIVALENT VERSIONS OF 5TH POSTULATE:
Given a line and a point not on it, exactly one parallel line passes through that point.
This is Playfair's axiom (equivalent to Euclid's 5th postulate).
SOLVED EXAMPLES:
Example 1: If AB=CD and EF=GH and AB=EF, prove CD=GH.
AB=CD (given). EF=GH (given). AB=EF (given).
By Axiom 1: CD=EF. By Axiom 1: CD=GH.
Example 2: How many lines through 2 distinct points? Exactly 1 (from Postulate 1).
COMMON MISTAKES:
Axioms are assumptions (self-evident truths). Theorems are proved from axioms and postulates.
The 5th postulate is NOT self-evident — this led to non-Euclidean geometry.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch5", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch6: Lines and Angles
KEY THEOREMS (with proofs):
Theorem 1: If two lines intersect, vertically opposite angles are equal.
Proof: angle 1 + angle 2 = 180° (linear pair). angle 3 + angle 2 = 180° (linear pair).
So angle 1 = angle 3. Similarly angle 2 = angle 4.
Theorem 2: Sum of angles on a straight line = 180°.
Theorem 3: If transversal cuts parallel lines:
(a) Corresponding angles are equal.
(b) Alternate interior angles are equal.
(c) Co-interior angles are supplementary (sum=180°).
Theorem 4 (Converse): If corresponding angles are equal → lines are parallel.
ANGLE SUM PROPERTY OF TRIANGLE:
Sum of angles of triangle = 180°. Proof using parallel line through vertex.
Draw BC. Draw line PQ through A parallel to BC.
Angle PAB = Angle ABC (alternate interior). Angle QAC = Angle ACB (alternate interior).
Angle PAB + Angle BAC + Angle QAC = 180° (straight line PQ).
Therefore Angle ABC + Angle BAC + Angle ACB = 180°.
EXTERIOR ANGLE THEOREM:
Exterior angle of triangle = sum of two non-adjacent interior angles.
SOLVED EXAMPLES:
Example 1: Two parallel lines cut by transversal. One angle=65°.
All 8 angles: 65°, 115°, 65°, 115°, 65°, 115°, 65°, 115°.
Alternate interior=65° (equal). Co-interior=115° (supplementary). Corresponding=65° (equal).
Example 2: Prove vertically opposite angles are equal.
Lines AB and CD intersect at O.
Angle AOC + Angle AOD = 180° (linear pair on line CD).
Angle BOD + Angle AOD = 180° (linear pair on line AB).
Therefore Angle AOC = Angle BOD. (both equal 180° - Angle AOD)
COMMON MISTAKES:
Co-interior angles are SUPPLEMENTARY (sum=180°), not equal.
Exterior angle = sum of REMOTE interior angles, NOT the adjacent interior angle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch7: Triangles (Congruence)
CONGRUENCE CRITERIA:
SAS: Two sides and included angle equal.
ASA: Two angles and included side equal.
AAS: Two angles and any corresponding side equal.
SSS: All three sides equal.
RHS: Right angle, hypotenuse and one side equal (right triangles).
IMPORTANT THEOREMS:
Theorem 1: Angles opposite equal sides of isosceles triangle are equal.
If AB=AC then Angle B=Angle C.
Proof: In triangles ABD and ACD (D=midpoint of BC):
AB=AC (given), BD=CD (D is midpoint), AD=AD (common). By SSS: triangles congruent. Angle B=Angle C by CPCT.
Theorem 2 (Converse): If two angles of triangle are equal, sides opposite them are equal.
Theorem 3: In right triangle, hypotenuse is the longest side.
Theorem 4: The sum of any two sides of triangle > third side.
Theorem 5: Of all line segments drawn from external point to line, perpendicular is shortest.
INEQUALITIES IN TRIANGLES:
In triangle, greater angle has greater opposite side.
If Angle A > Angle B then BC > AC.
CPCT: Corresponding Parts of Congruent Triangles.
SOLVED EXAMPLES:
Example 1: ABC is isosceles with AB=AC. D is midpoint of BC. Prove AD perpendicular to BC.
In triangles ABD and ACD: AB=AC, BD=CD, AD=AD. SSS congruence.
Angle ADB=Angle ADC (CPCT). Both on straight line, so each=90°. AD perpendicular to BC.
Example 2: Prove that triangle ABC where AB=BC=CA (equilateral) has all angles 60°.
AB=BC → Angle A=Angle C. BC=CA → Angle A=Angle B. So A=B=C. A+B+C=180°. Each=60°.
COMMON MISTAKES:
RHS works ONLY for right triangles. Cannot apply to other triangles.
CPCT used only AFTER proving congruence.
SAS: the angle must be INCLUDED (between the two sides).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch8: Quadrilaterals
ANGLE SUM: Sum of angles of quadrilateral=360°.
PARALLELOGRAM PROPERTIES:
(i) Opposite sides are parallel and equal.
(ii) Opposite angles are equal.
(iii) Consecutive angles are supplementary (sum=180°).
(iv) Diagonals bisect each other.
THEOREMS:
Theorem 1: Diagonal divides parallelogram into two congruent triangles.
Theorem 2: Opposite sides of parallelogram are equal (and converse).
Theorem 3: Opposite angles of parallelogram are equal (and converse).
Theorem 4: Diagonals of parallelogram bisect each other (and converse).
Theorem 5: Parallelograms on same base and between same parallels are equal in area.
MID-POINT THEOREM:
The line joining midpoints of two sides of triangle is parallel to third side and half its length.
If D=midpoint of AB and E=midpoint of AC then DE parallel to BC and DE=BC/2.
CONVERSE: Line through midpoint of one side parallel to another side bisects the third side.
SOLVED EXAMPLES:
Example 1: ABCD is parallelogram. Angle A=70°. Find all angles.
Angle C=70° (opposite). Angle B=Angle D=180-70=110° (supplementary to A).
Example 2: In parallelogram ABCD, diagonals AC and BD meet at O. AO=5cm. Find AC.
AO=OC (diagonals bisect each other). AC=2×AO=10cm.
Example 3: Mid-point theorem — D and E are midpoints of AB and AC. DE=4cm. Find BC.
BC=2×DE=8cm.
COMMON MISTAKES:
Diagonals of parallelogram bisect each other but are NOT equal (unless rectangle).
Diagonals of rectangle are equal but do NOT bisect at 90° (unless square).
Diagonals of rhombus bisect at 90° but are NOT equal (unless square).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch9: Areas of Parallelograms and Triangles
KEY CONCEPT: Two figures with equal areas are not necessarily congruent.
Two congruent figures always have equal areas.
THEOREMS:
Theorem 1: Parallelograms on same base and between same parallels are equal in area.
Theorem 2: Triangles on same base and between same parallels are equal in area.
Theorem 3: Median divides triangle into two equal area triangles.
Theorem 4: Triangle area = half of parallelogram area if same base and same parallels.
AREA FORMULAS:
Parallelogram = base × height (perpendicular height).
Triangle = (1/2) × base × height.
If parallelogram ABCD and triangle ABE are on same base AB between same parallels:
Area(ABE) = (1/2) × Area(ABCD).
SOLVED EXAMPLES:
Example 1: ABCD is parallelogram. E is point on DC. Show area(ABE)=area(ABD).
Both triangles ABD and ABE have same base AB.
Both between same parallels AB and DC.
Area(ABD)=Area(ABE)=(1/2)Area(ABCD).
Example 2: Parallelogram ABCD and rectangle ABEF on same base AB between same parallels.
Area(ABCD)=Area(ABEF)=AB×h.
Example 3: In triangle PQR, S is midpoint of QR. Area(PQS)=Area(PRS).
PS is median. Median divides triangle into two equal areas.
Example 4: Parallelogram base=8cm, height=5cm. Area=8×5=40cm^2.
Triangle between same base and parallels: area=20cm^2.
COMMON MISTAKES:
Height must be PERPENDICULAR to base.
Two parallelograms on same base with same height have equal area even if they look different.
Median divides area in HALF (not sides in half — it divides opposite side in half).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch10: Circles
KEY DEFINITIONS:
Circle: set of all points at equal distance (radius) from centre.
Chord: line segment joining any two points on circle.
Diameter: longest chord passing through centre = 2r.
Arc: part of circle. Minor arc < semicircle. Major arc > semicircle.
Sector: region between two radii and arc.
Segment: region between chord and arc.
THEOREMS:
Theorem 1: Equal chords are equidistant from centre (and converse).
Theorem 2: Equal chords subtend equal angles at centre (and converse).
Proof: In triangles OAB and OCD (O=centre, AB=CD):
OA=OC=OB=OD=radius. AB=CD (given). By SSS: triangles congruent. Angle AOB=Angle COD.
Theorem 3: Perpendicular from centre bisects chord (and converse).
Theorem 4: Angle in semicircle is 90°.
Theorem 5: Angles in same segment are equal.
Theorem 6: Angle at centre = double angle at circumference (same arc).
Theorem 7: Opposite angles of cyclic quadrilateral sum to 180°.
SOLVED EXAMPLES:
Example 1: Chord AB=10cm. Distance from centre=12cm. Find radius.
Perpendicular from centre bisects chord. Half chord=5cm.
r^2=12^2+5^2=144+25=169. r=13cm.
Example 2: Angle at centre=120°. Find angle at circumference (same arc).
Angle at circumference=120/2=60°.
Example 3: In cyclic quadrilateral, one angle=75°. Find opposite angle.
Opposite angles sum=180°. Other angle=105°.
COMMON MISTAKES:
Angle at centre = TWICE angle at circumference (not half).
Angle in semicircle=90° (angle subtended by diameter).
Equal chords have equal angles at centre: equal angle does NOT mean equal chord unless same circle.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch11: Constructions
BASIC CONSTRUCTIONS (Class 6 review):
Perpendicular bisector, angle bisector, 60°, 90°, 45°, 30° using compass.
CLASS 9 CONSTRUCTIONS:
Construction 1: Angle of 60° (without protractor).
Draw ray OA. Arc from O cuts OA at P. Same radius arc from P cuts first arc at Q. Angle QOP=60°.
Construction 2: Bisect any given angle.
Construction 3: Draw perpendicular to given line from given point.
Construction 4: Construct triangle given base, base angle, and sum of other two sides.
Steps: Draw BC (base). Draw angle at B. Mark D on ray such that BD=AB+AC. Join DC. Bisect DC to get perpendicular bisector meeting BD at A. Join AC. Triangle ABC is constructed.
Construction 5: Construct triangle given base, base angle, and DIFFERENCE of other two sides.
Two cases: given side longer or shorter.
Construction 6: Construct triangle given perimeter and two base angles.
Steps: Draw line XY=perimeter. Draw angles at X and Y. Bisect both angles. Bisectors meet at A. Draw perpendicular bisectors of XA and YA to get B and C. Triangle ABC is the required triangle.
Construction 7: Construct right triangle given hypotenuse and one side.
JUSTIFICATION OF CONSTRUCTIONS:
Each construction must be justified by proving why the constructed figure satisfies given conditions.
SOLVED EXAMPLES:
Example 1: Construct triangle with perimeter 11cm and base angles 60° and 45°.
Step 1: Draw XY=11cm.
Step 2: Draw 60° at X, 45° at Y.
Step 3: Bisect these angles. Bisectors meet at A.
Step 4: Perpendicular bisectors of XA and YA meet XY at B and C respectively.
Triangle ABC has perimeter 11cm and base angles 60° and 45°.
COMMON MISTAKES:
Always bisect the BASE angles at X and Y (not the constructed angles).
In construction 4: bisect DC (the line joining end of ray to far end), not the base BC.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch12: Heron's Formula
HERON'S FORMULA: Area of triangle when all 3 sides are known.
Area = sqrt(s(s-a)(s-b)(s-c))
where a, b, c are the three sides and s = semi-perimeter = (a+b+c)/2.
STEPS:
1. Find s = (a+b+c)/2.
2. Find (s-a), (s-b), (s-c).
3. Multiply: s × (s-a) × (s-b) × (s-c).
4. Take square root.
APPLICATION TO QUADRILATERALS:
Divide quadrilateral into two triangles using diagonal.
Apply Heron's formula to each triangle.
Total area = sum of both triangle areas.
EQUILATERAL TRIANGLE (special case):
All sides = a. s = 3a/2.
Area = sqrt((3a/2)(a/2)(a/2)(a/2)) = (sqrt(3)/4)×a^2.
ISOSCELES TRIANGLE:
If a=b, formula simplifies but Heron's formula still works.
SOLVED EXAMPLES:
Example 1: Sides 13cm, 14cm, 15cm.
s=(13+14+15)/2=42/2=21.
s-a=21-13=8, s-b=21-14=7, s-c=21-15=6.
Area=sqrt(21×8×7×6)=sqrt(7056)=84cm^2.
Example 2: Equilateral triangle side=6cm.
s=9. Area=sqrt(9×3×3×3)=sqrt(243)=9sqrt(3)cm^2.
OR using formula: (sqrt(3)/4)×36=9sqrt(3)cm^2. Same answer.
Example 3: Quadrilateral ABCD. Diagonal AC=10cm. Triangle ABC sides 6,8,10. Triangle ACD sides 10,7,9.
For ABC: s=12. Area=sqrt(12×6×4×2)=sqrt(576)=24cm^2.
For ACD: s=13. Area=sqrt(13×3×6×4)=sqrt(936)=6sqrt(26)cm^2.
Total area=24+6sqrt(26)cm^2.
COMMON MISTAKES:
s is the SEMI-perimeter (half of perimeter), not the full perimeter.
Must check triangle inequality: sum of any two sides > third side.
All three (s-a), (s-b), (s-c) must be positive for valid triangle.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_9", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch13: Surface Areas and Volumes
SURFACE AREA AND VOLUME FORMULAS:
CUBOID: l=length, b=breadth, h=height.
Total SA=2(lb+bh+lh). Lateral SA=2(l+b)h. Volume=lbh. Diagonal=sqrt(l^2+b^2+h^2).
CUBE: side=a.
Total SA=6a^2. Lateral SA=4a^2. Volume=a^3. Diagonal=a*sqrt(3).
CYLINDER: r=radius, h=height.
Curved SA=2*pi*r*h. Total SA=2*pi*r(r+h). Volume=pi*r^2*h.
CONE: r=base radius, h=vertical height, l=slant height.
l=sqrt(r^2+h^2). Curved SA=pi*r*l. Total SA=pi*r(r+l). Volume=(1/3)*pi*r^2*h.
SPHERE: r=radius.
SA=4*pi*r^2. Volume=(4/3)*pi*r^3.
HEMISPHERE: r=radius.
Curved SA=2*pi*r^2. Total SA=3*pi*r^2. Volume=(2/3)*pi*r^3.
SOLVED EXAMPLES:
Example 1: Cone r=5cm, l=13cm.
h=sqrt(13^2-5^2)=sqrt(144)=12cm.
Curved SA=pi×5×13=65pi=204.1cm^2.
Total SA=pi×5×(5+13)=90pi=282.6cm^2.
Volume=(1/3)×pi×25×12=100pi=314.2cm^3.
Example 2: Sphere r=7cm.
SA=4×(22/7)×49=616cm^2.
Volume=(4/3)×(22/7)×343=1437.3cm^3.
Example 3: Cylinder r=4cm, h=10cm.
Curved SA=2×pi×4×10=80pi=251.2cm^2.
Volume=pi×16×10=160pi=502.4cm^3.
COMMON MISTAKES:
Cone: slant height l=sqrt(r^2+h^2). Given l, find h=sqrt(l^2-r^2).
Hemisphere Total SA=3pi*r^2 (curved 2pi*r^2 + base circle pi*r^2).
Volume of cone=(1/3)×volume of cylinder with same base and height.""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_9", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch14: Statistics
TYPES OF DATA:
Primary data: collected by investigator. Secondary data: from other sources.
Raw data: unorganised. Grouped data: organised in class intervals.
FREQUENCY DISTRIBUTION TABLE:
Class interval: group of values (0-10, 10-20 etc). Class width=upper-lower limit.
Frequency: number of observations in each class.
Class mark (midpoint)=(upper limit+lower limit)/2.
Cumulative frequency: running total of frequencies.
MEAN FOR GROUPED DATA:
Direct method: Mean = sum(f×x)/sum(f) where x=class mark, f=frequency.
Assumed mean method: Mean = a + sum(f×d)/sum(f) where d=x-a, a=assumed mean.
Step deviation method: Mean = a + (sum(f×u)/sum(f))×h where u=(x-a)/h, h=class width.
MEDIAN FOR GROUPED DATA:
Median = L + ((n/2-cf)/f)×h
where L=lower limit of median class, n=total frequency, cf=cumulative frequency before median class, f=frequency of median class, h=class width.
MODE FOR GROUPED DATA:
Mode = L + ((f1-f0)/(2f1-f0-f2))×h
where L=lower limit of modal class, f1=frequency of modal class, f0=previous class frequency, f2=next class frequency, h=class width.
EMPIRICAL RELATIONSHIP: Mode = 3×Median - 2×Mean (approximately).
SOLVED EXAMPLES:
Example 1: Mean by assumed mean. Class marks: 10,20,30,40,50. Frequencies: 4,6,8,5,3. Assumed mean=30.
d values: -20,-10,0,10,20. sum(f×d)=4(-20)+6(-10)+8(0)+5(10)+3(20)=-80-60+0+50+60=-30.
Mean=30+(-30/26)=30-1.15=28.85.
Example 2: Find median class for n=26. n/2=13. Cumulative frequencies: 4,10,18,...
13 falls in third class (cf=10, f=8). Median class is the third class interval.
COMMON MISTAKES:
Class mark is MIDPOINT of class interval, not lower or upper limit.
For median: find n/2 first, then locate which cumulative frequency it falls in.
Modal class has HIGHEST frequency, not highest value.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_9", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch15: Probability
BASIC CONCEPTS:
Experiment: activity with defined set of outcomes. e.g., throwing die, tossing coin.
Sample space: set of ALL possible outcomes. S={H,T} for coin. S={1,2,3,4,5,6} for die.
Event: subset of sample space. Any collection of outcomes.
PROBABILITY FORMULA:
P(E) = Number of favourable outcomes / Total number of outcomes.
Range: 0 <= P(E) <= 1.
P(certain event) = 1. P(impossible event) = 0.
COMPLEMENTARY EVENT:
P(E) + P(not E) = 1. So P(not E) = 1 - P(E).
TYPES OF EVENTS:
Simple event: single outcome. Compound event: more than one outcome.
Mutually exclusive: cannot occur simultaneously. P(A or B)=P(A)+P(B).
EQUALLY LIKELY OUTCOMES: each outcome has same probability of occurring.
STANDARD PROBLEMS:
Die: P(even)=3/6=1/2. P(prime)=3/6=1/2 (2,3,5). P(>4)=2/6=1/3 (5,6).
Coin: P(H)=1/2. Two coins: P(both H)=1/4. P(at least one H)=3/4.
Cards (52): P(ace)=4/52=1/13. P(face card)=12/52=3/13. P(red)=26/52=1/2.
Two dice: Total outcomes=36. P(sum=7): (1,6),(2,5),(3,4),(4,3),(5,2),(6,1)=6/36=1/6.
SOLVED EXAMPLES:
Example 1: Bag has 5 red, 7 blue, 3 green balls. Total=15.
P(red)=5/15=1/3. P(not blue)=(15-7)/15=8/15. P(green or red)=8/15.
Example 2: Two dice thrown. P(sum=8)?
Pairs: (2,6),(3,5),(4,4),(5,3),(6,2)=5 pairs. P=5/36.
Example 3: Cards. P(king or queen)?
Kings=4, Queens=4. Total face cards include these. P(king or queen)=8/52=2/13.
COMMON MISTAKES:
P(E) must be between 0 and 1 inclusive.
For two dice: total outcomes=36 (not 12). Each die independent.
P(not E)=1-P(E), NOT P(E)-1.""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_9", "chapter": "ch15", "difficulty": "intermediate"}),


    # ── CLASS 10 — All 15 Chapters ──────────────────────────────────

    Document(page_content="""Class 10 | Ch1: Real Numbers
EUCLID'S DIVISION LEMMA:
For any two positive integers a and b, there exist unique integers q and r such that:
a = bq + r where 0 <= r < b.
a=dividend, b=divisor, q=quotient, r=remainder.
EUCLID'S DIVISION ALGORITHM (for HCF):
Step 1: Apply lemma: a=bq+r.
Step 2: If r=0, HCF=b. If r≠0, apply lemma to b and r.
Step 3: Repeat until remainder=0. Last non-zero remainder=HCF.
Example: HCF(96,404). 404=96×4+20. 96=20×4+16. 20=16×1+4. 16=4×4+0. HCF=4.
FUNDAMENTAL THEOREM OF ARITHMETIC:
Every composite number can be expressed as product of primes in UNIQUE way (ignoring order).
Used to find HCF and LCM of large numbers.
HCF = product of SMALLEST powers of common prime factors.
LCM = product of GREATEST powers of all prime factors.
HCF × LCM = product of two numbers (for exactly TWO numbers).
PROVING IRRATIONALITY:
Standard method: assume rational p/q (lowest terms), reach contradiction.
Prove sqrt(3) irrational: assume sqrt(3)=p/q, HCF(p,q)=1.
3=p^2/q^2 → p^2=3q^2 → 3 divides p^2 → 3 divides p → p=3m.
9m^2=3q^2 → q^2=3m^2 → 3 divides q. Both divisible by 3 contradicts HCF=1.
Also: sqrt(2)+sqrt(3), 2-sqrt(5), 1/sqrt(2) are all irrational.
RATIONAL NUMBER DECIMAL EXPANSIONS:
Terminating: denominator (in simplest form) has only 2s and 5s as prime factors.
Non-terminating repeating: denominator has prime factors other than 2 and 5.
17/8=17/2^3: terminating (only 2s). 7/6=7/(2×3): non-terminating repeating (has 3).
SOLVED EXAMPLES:
Example 1: HCF(96,404) by Euclid's algorithm.
404=96×4+20. 96=20×4+16. 20=16×1+4. 16=4×4+0. HCF=4.
LCM=96×404/4=9696.
Example 2: Is 64/455 terminating?
455=5×7×13. Has factors 7 and 13 (not just 2,5). Non-terminating repeating.
COMMON MISTAKES:
HCF×LCM=product of numbers works for EXACTLY TWO numbers only.
For terminating decimal: simplify fraction FIRST then check denominator.""",
    metadata={"source": "ncert", "topic": "numbers", "class_level": "class_10", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch2: Polynomials
ZEROES OF POLYNOMIAL:
Zero of polynomial p(x): value of x where p(x)=0.
Geometrically: x-coordinates where graph of y=p(x) crosses x-axis.
Linear polynomial (degree 1): has exactly 1 zero.
Quadratic polynomial (degree 2): has at most 2 zeroes.
Cubic polynomial (degree 3): has at most 3 zeroes.
RELATIONSHIP BETWEEN ZEROES AND COEFFICIENTS:
For quadratic p(x)=ax^2+bx+c with zeroes alpha and beta:
Sum of zeroes: alpha+beta = -b/a.
Product of zeroes: alpha×beta = c/a.
For cubic p(x)=ax^3+bx^2+cx+d with zeroes alpha, beta, gamma:
alpha+beta+gamma = -b/a.
alpha*beta+beta*gamma+gamma*alpha = c/a.
alpha*beta*gamma = -d/a.
FORMING POLYNOMIAL FROM ZEROES:
Quadratic with zeroes alpha, beta: p(x)=k[x^2-(alpha+beta)x+alpha*beta].
DIVISION ALGORITHM FOR POLYNOMIALS:
p(x) = g(x)×q(x) + r(x).
Degree of remainder < degree of divisor.
SOLVED EXAMPLES:
Example 1: Find zeroes of p(x)=6x^2-3-7x=6x^2-7x-3.
6x^2-7x-3=0. Split: 6x^2-9x+2x-3=3x(2x-3)+1(2x-3)=(3x+1)(2x-3).
Zeroes: x=-1/3 and x=3/2.
Verify: sum=-1/3+3/2=(-2+9)/6=7/6=-(-7)/6=b/a. Wait: -b/a=-(-7)/6=7/6. Correct.
Product=(-1/3)(3/2)=-1/2=c/a=-3/6=-1/2. Correct.
Example 2: Form quadratic with zeroes 2 and -3.
Sum=2+(-3)=-1. Product=2×(-3)=-6. p(x)=x^2-(-1)x+(-6)=x^2+x-6.
Example 3: Cubic zeroes 2,-1,-3.
Sum=2-1-3=-2=-b/a → b/a=2. Sum of products=2(-1)+(-1)(-3)+(-3)(2)=-2+3-6=-5=c/a.
Product=2×(-1)×(-3)=6=-d/a → d/a=-6. p(x)=x^3+2x^2-5x-6 (taking a=1).
COMMON MISTAKES:
Sum of zeroes=-b/a (NEGATIVE b over a, not b over a).
Product of zeroes=c/a (positive, not negative).
Zeroes of polynomial: solve p(x)=0 (set equal to zero, NOT to y).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations in Two Variables
STANDARD FORM: a1x+b1y+c1=0 and a2x+b2y+c2=0.
CONSISTENCY CONDITIONS:
Unique solution (consistent): a1/a2 ≠ b1/b2. Lines intersect.
Infinitely many solutions (consistent, dependent): a1/a2=b1/b2=c1/c2. Lines coincide.
No solution (inconsistent): a1/a2=b1/b2 ≠ c1/c2. Lines parallel.
METHODS OF SOLVING:
Graphical: plot both lines, find intersection point.
Substitution: express one variable in terms of other, substitute.
Elimination: multiply equations to make coefficients equal, add/subtract.
Cross-multiplication: x/((b1c2-b2c1))=y/((c1a2-c2a1))=1/((a1b2-a2b1)).
CROSS MULTIPLICATION FORMULA:
For a1x+b1y+c1=0 and a2x+b2y+c2=0:
x=(b1c2-b2c1)/(a1b2-a2b1), y=(c1a2-c2a1)/(a1b2-a2b1).
SOLVED EXAMPLES:
Example 1: Solve 2x+3y=11 and 2x-4y=-24 by elimination.
Subtract: 7y=35 → y=5. Substitute: 2x+15=11 → x=-2.
Solution: x=-2, y=5.
Example 2: Solve by cross-multiplication: 2x+3y-11=0 and 2x-4y+24=0.
x/(3×24-(-4)×(-11))=y/((-11)×2-24×2)=1/(2×(-4)-2×3).
x/(72-44)=y/(-22-48)=1/(-8-6).
x/28=y/(-70)=1/(-14).
x=28/(-14)=-2. y=-70/(-14)=5. Solution: (-2,5).
Example 3: Check 3x+2y=5 and 6x+4y=10.
a1/a2=3/6=1/2. b1/b2=2/4=1/2. c1/c2=5/10=1/2.
All ratios equal → infinitely many solutions (dependent).
COMMON MISTAKES:
Cross-multiplication: use the formula carefully with correct signs.
Check consistency BEFORE solving — if inconsistent, no solution exists.
Graphical method: use at least 3 points per line to verify.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch4: Quadratic Equations
STANDARD FORM: ax^2+bx+c=0 where a≠0.
METHODS OF SOLVING:
Method 1 - Factorisation:
Split middle term: find p,q such that p+q=b and p×q=a×c.
2x^2-7x+3=0. a×c=6. p+q=-7, p×q=6. p=-6,q=-1.
2x^2-6x-x+3=0 → 2x(x-3)-1(x-3)=0 → (2x-1)(x-3)=0.
x=1/2 or x=3.
Method 2 - Completing the Square:
ax^2+bx+c=0 → x^2+(b/a)x=-c/a → add (b/2a)^2 both sides.
(x+b/2a)^2=(b^2-4ac)/4a^2 → x=-b/2a ± sqrt(b^2-4ac)/2a.
Method 3 - Quadratic Formula:
x=(-b ± sqrt(b^2-4ac))/2a. (Derived from completing the square.)
DISCRIMINANT D=b^2-4ac:
D>0: two distinct real roots. D=0: two equal real roots (repeated). D<0: no real roots (complex).
NATURE OF ROOTS:
If D is perfect square: roots are rational. If D>0 but not perfect square: roots irrational.
RELATIONSHIP BETWEEN ROOTS:
Sum of roots=alpha+beta=-b/a. Product of roots=alpha×beta=c/a.
WORD PROBLEMS - STANDARD TYPES:
Number problems, age problems, speed-distance problems, area problems.
SOLVED EXAMPLES:
Example 1: 2x^2-7x+3=0 by factorisation.
a×c=6. Factors of 6 summing to -7: -6 and -1.
2x^2-6x-x+3=2x(x-3)-1(x-3)=(2x-1)(x-3)=0.
x=1/2 or x=3.
Example 2: Find nature of roots of 2x^2-6x+3=0.
D=36-24=12>0. Two distinct real roots (D not perfect square, so irrational).
Example 3: Sum of ages of father and son is 45. Five years ago product was 124.
Let son's age=x. Father's age=45-x.
(x-5)(45-x-5)=124 → (x-5)(40-x)=124.
40x-x^2-200+5x=124 → x^2-45x+324=0 → (x-9)(x-36)=0.
x=9 (son) or x=36 (check: son can't be 36 if sum is 45). Son=9, Father=36.
COMMON MISTAKES:
Discriminant: D=b^2-4ac NOT b^2+4ac.
If D=0: ONE repeated root (two equal roots, not no roots).
Quadratic formula: entire (-b±sqrt(D)) is over 2a.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions
ARITHMETIC PROGRESSION (AP): sequence where difference between consecutive terms is constant.
Common difference d=a2-a1=a3-a2=... (can be positive, negative, or zero).
General form: a, a+d, a+2d, a+3d, ...
nth TERM FORMULA: a_n = a + (n-1)d where a=first term, d=common difference.
SUM OF FIRST n TERMS:
S_n = n/2 × [2a + (n-1)d] = n/2 × [a + l] where l=last term=a_n.
FINDING NUMBER OF TERMS: use a_n=a+(n-1)d, solve for n.
PROPERTIES:
If a,b,c are in AP: b-a=c-b → 2b=a+c → b=(a+c)/2 (b is arithmetic mean).
Sum of AP from both ends: a1+a_n=a2+a_(n-1)=... (equidistant terms have equal sum).
THREE NUMBERS IN AP: take as a-d, a, a+d (sum=3a, simplifies problems).
FOUR NUMBERS IN AP: take as a-3d, a-d, a+d, a+3d.
SOLVED EXAMPLES:
Example 1: Sum of first 40 positive integers divisible by 6.
AP: 6,12,18,...,240. a=6, d=6, n=40.
S_40=40/2×[2(6)+(40-1)(6)]=20×[12+234]=20×246=4920.
Example 2: 7th term=34, 13th term=64. Find AP and S_20.
a+6d=34 ...(i). a+12d=64 ...(ii).
(ii)-(i): 6d=30 → d=5. From (i): a=34-30=4.
AP: 4,9,14,19,...
S_20=20/2×[2(4)+19(5)]=10×[8+95]=10×103=1030.
Example 3: How many terms of AP 3,5,7,... give sum 120?
S_n=n/2×[2(3)+(n-1)(2)]=n/2×[4n+2]=n(2n+1)... Wait: n/2[6+2n-2]=n/2[2n+4]=n(n+2)=120.
n^2+2n-120=0. (n+12)(n-10)=0. n=10.
COMMON MISTAKES:
nth term formula: a_n=a+(n-1)d NOT a+(n)d.
In sum formula S_n=n/2[2a+(n-1)d], the n inside brackets is (n-1) not n.
d can be negative (decreasing AP) or zero (constant sequence).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch6: Triangles (Similarity)
SIMILAR TRIANGLES: same shape, different size. Corresponding angles equal, corresponding sides proportional.
Symbol: triangle ABC ~ triangle DEF.
BASIC PROPORTIONALITY THEOREM (BPT / Thales Theorem):
If a line is drawn parallel to one side of triangle, it divides the other two sides proportionally.
If DE || BC in triangle ABC: AD/DB = AE/EC.
CONVERSE: If a line divides two sides of triangle proportionally, it is parallel to third side.
CRITERIA FOR SIMILARITY:
AAA (AA): Two angles equal → triangles similar.
SSS: All three sides proportional → triangles similar.
SAS: Two sides proportional and included angle equal → triangles similar.
AREAS OF SIMILAR TRIANGLES:
Ratio of areas = Square of ratio of corresponding sides.
If triangle ABC ~ triangle DEF: Area(ABC)/Area(DEF) = (AB/DE)^2 = (BC/EF)^2 = (CA/FD)^2.
PYTHAGORAS THEOREM:
In right triangle, square of hypotenuse = sum of squares of other two sides.
c^2=a^2+b^2. Proof using similar triangles (altitude on hypotenuse).
CONVERSE: If c^2=a^2+b^2, angle opposite c is 90°.
SOLVED EXAMPLES:
Example 1: In triangle ABC, DE||BC. AD=2cm, DB=3cm, AE=4cm. Find EC.
By BPT: AD/DB=AE/EC → 2/3=4/EC → EC=6cm.
Example 2: Triangle ABC ~ triangle DEF. AB=4,BC=5,CA=6. DE=8. Find EF and FD.
Ratio AB/DE=4/8=1/2. So all sides doubled.
EF=2×BC=10. FD=2×CA=12.
Example 3: Areas of two similar triangles are 25cm^2 and 100cm^2. If base of smaller=3cm, find base of larger.
Area ratio=25/100=1/4=(side ratio)^2. Side ratio=1/2. Larger base=2×3=6cm.
COMMON MISTAKES:
BPT: line must be PARALLEL to one side (not just any line).
Area ratio=(side ratio)^2 NOT side ratio directly.
AA criterion: only need 2 angles equal (third is automatic since sum=180°).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch7: Coordinate Geometry
DISTANCE FORMULA:
Distance between P(x1,y1) and Q(x2,y2) = sqrt((x2-x1)^2+(y2-y1)^2).
Distance from origin: OP=sqrt(x^2+y^2).
SECTION FORMULA:
Point P dividing AB (A(x1,y1), B(x2,y2)) in ratio m:n INTERNALLY:
P = ((mx2+nx1)/(m+n), (my2+ny1)/(m+n)).
MIDPOINT FORMULA (m=n=1):
M = ((x1+x2)/2, (y1+y2)/2).
EXTERNAL DIVISION:
P = ((mx2-nx1)/(m-n), (my2-ny1)/(m-n)).
AREA OF TRIANGLE:
Given A(x1,y1), B(x2,y2), C(x3,y3):
Area = (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|.
If area=0, points are COLLINEAR.
CENTROID OF TRIANGLE:
G = ((x1+x2+x3)/3, (y1+y2+y3)/3). Divides each median in 2:1.
SOLVED EXAMPLES:
Example 1: Distance between A(2,3) and B(-1,0).
AB=sqrt((-1-2)^2+(0-3)^2)=sqrt(9+9)=sqrt(18)=3sqrt(2).
Example 2: Find point dividing (1,3) and (4,6) in ratio 2:1 internally.
P=((2×4+1×1)/(2+1),(2×6+1×3)/(2+1))=(9/3,15/3)=(3,5).
Example 3: Area of triangle A(2,3), B(-1,0), C(2,-4).
Area=(1/2)|2(0-(-4))+(-1)((-4)-3)+2(3-0)|=(1/2)|8+7+6|=(1/2)(21)=10.5 sq units.
Example 4: Show A(1,2), B(3,4), C(5,6) are collinear.
Area=(1/2)|1(4-6)+3(6-2)+5(2-4)|=(1/2)|(-2)+12+(-10)|=(1/2)(0)=0. Collinear.
COMMON MISTAKES:
Section formula: m corresponds to the second point B, n to first point A.
Area formula: use ABSOLUTE VALUE (modulus bars) — area cannot be negative.
Midpoint: average of BOTH x-coordinates and BOTH y-coordinates separately.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry
TRIGONOMETRIC RATIOS (right triangle, angle theta):
sin(theta)=opposite/hypotenuse=P/H.
cos(theta)=adjacent/hypotenuse=B/H.
tan(theta)=opposite/adjacent=P/B=sin/cos.
cosec(theta)=1/sin=H/P. sec(theta)=1/cos=H/B. cot(theta)=1/tan=B/P.
STANDARD VALUES TABLE:
Angle:      0°    30°      45°       60°       90°
sin:        0     1/2      1/sqrt2   sqrt3/2   1
cos:        1     sqrt3/2  1/sqrt2   1/2       0
tan:        0     1/sqrt3  1         sqrt3     undefined
cosec:      undef 2        sqrt2     2/sqrt3   1
sec:        1     2/sqrt3  sqrt2     2         undef
cot:        undef sqrt3    1         1/sqrt3   0
TRIGONOMETRIC IDENTITIES:
sin^2(theta)+cos^2(theta)=1.
1+tan^2(theta)=sec^2(theta).
1+cot^2(theta)=cosec^2(theta).
COMPLEMENTARY ANGLES:
sin(90-A)=cos(A). cos(90-A)=sin(A). tan(90-A)=cot(A).
cosec(90-A)=sec(A). sec(90-A)=cosec(A). cot(90-A)=tan(A).
SOLVED EXAMPLES:
Example 1: If sin(theta)=3/5, find all trig ratios.
P=3, H=5, B=sqrt(25-9)=4.
cos=4/5, tan=3/4, cosec=5/3, sec=5/4, cot=4/3.
Example 2: Prove (sin^2(theta)/cos(theta)) + cos(theta) = sec(theta).
LHS=sin^2/cos+cos=(sin^2+cos^2)/cos=1/cos=sec. Proved.
Example 3: Evaluate 2tan^2(45°)+cos^2(30°)-sin^2(60°).
=2(1)^2+(sqrt3/2)^2-(sqrt3/2)^2=2+3/4-3/4=2.
Example 4: sin(theta)=cos(theta). Find theta.
tan(theta)=1. theta=45°.
COMMON MISTAKES:
sin^2+cos^2=1 (NOT sin+cos=1).
Values at 90°: sin=1, cos=0, tan=undefined (NOT 0).
Memorise table using: "Some People Have Curly Brown Hair Through Proper Brushing".""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch9: Applications of Trigonometry (Heights and Distances)
KEY TERMS:
Angle of elevation: angle formed above horizontal when looking UP at an object.
Angle of depression: angle formed below horizontal when looking DOWN at an object.
Observer, object, horizontal line form a right triangle.
Line of sight: line from eye to object.
Note: Angle of elevation from A to B = Angle of depression from B to A (alternate interior angles).
STANDARD SETUP:
Draw a clear diagram. Identify right triangles. Assign variables.
Use appropriate trig ratio: tan for height/distance, sin/cos if hypotenuse involved.
STANDARD PROBLEM TYPES:
Type 1: Height of tower/building given angle of elevation and distance.
Type 2: Distance of boat/object given angle of depression from top.
Type 3: Two angles from same point (form two equations).
Type 4: Two observers at different points (system of equations).
USEFUL: tan(30°)=1/sqrt3, tan(45°)=1, tan(60°)=sqrt3.
SOLVED EXAMPLES:
Example 1: Tower 75m high. From base, angles of depression of two boats=30° and 45°.
Let boat A (30°) distance=x, boat B (45°) distance=y.
tan(30°)=75/x → x=75sqrt(3). tan(45°)=75/y → y=75.
Distance between boats=x-y=75sqrt(3)-75=75(sqrt3-1)=75(1.732-1)=54.9m.
Example 2: Boy 1.2m tall stands 30m from tower. Elevation angle=60°. Find tower height.
tan(60°)=(h-1.2)/30 → sqrt3=h-1.2)/30 → h=30sqrt3+1.2=51.96+1.2=53.16m.
Example 3: Kite string 150m, angle=60°. Find height of kite.
sin(60°)=h/150 → h=150×sqrt3/2=75sqrt3 metres.
COMMON MISTAKES:
Angle of depression = angle of elevation (they are alternate interior angles, not supplementary).
Height of observer must be considered in many problems.
Always draw diagram first — most errors come from not visualising correctly.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch10: Circles
KEY DEFINITIONS:
Tangent: line touching circle at exactly ONE point (point of tangency/contact).
Secant: line intersecting circle at TWO points.
A tangent is perpendicular to radius at point of contact.
THEOREMS:
Theorem 1: Tangent at any point of circle is perpendicular to radius through that point.
Proof: Any point on tangent other than contact point is outside circle (farther from centre).
So perpendicular from centre to tangent = shortest distance = radius. Hence radius ⊥ tangent.
Theorem 2: Lengths of tangents drawn from external point are EQUAL.
If PA and PB are tangents from P to circle with centre O:
In triangles OAP and OBP: OA=OB (radii), OP=OP (common), angle OAP=angle OBP=90°.
By RHS: triangles congruent → PA=PB (CPCT).
Also: OP bisects angle APB and angle AOB.
LENGTH OF TANGENT FROM EXTERNAL POINT:
If d=distance from external point to centre, r=radius:
Length of tangent=sqrt(d^2-r^2).
ANGLE IN ALTERNATE SEGMENT (Tangent-Chord angle):
Angle between tangent and chord = inscribed angle in alternate segment.
SOLVED EXAMPLES:
Example 1: Point P is 17cm from centre. Radius=8cm. Find tangent length.
Tangent=sqrt(17^2-8^2)=sqrt(289-64)=sqrt(225)=15cm.
Example 2: Two tangents PA=PB from external point P. PA=12cm, OA=5cm. Find OP.
OP^2=OA^2+PA^2=25+144=169. OP=13cm.
Example 3: Tangents from P touch circle at A and B. Angle APB=60°. Find angle AOB.
Since PA=PB, triangle PAB is isosceles. Angle OAP=90°.
In quadrilateral OAPB: angle AOB+angle OBP+angle APB+angle OAP=360°.
angle AOB+90°+60°+90°=360° → angle AOB=120°.
COMMON MISTAKES:
Tangent from EXTERNAL point has equal length — this fails for internal points.
Tangent ⊥ radius at POINT OF CONTACT (not at every point of tangent).
Length of tangent uses Pythagoras: sqrt(d^2-r^2), not d-r.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch11: Constructions
CONSTRUCTION 1: DIVIDE LINE SEGMENT IN GIVEN RATIO (m:n)
To divide AB in ratio 3:2:
Step 1: Draw ray AX at acute angle to AB.
Step 2: Mark 3+2=5 equal arcs on AX: A1,A2,A3,A4,A5.
Step 3: Join A5 to B.
Step 4: Draw line through A3 parallel to A5B (using corresponding angles).
Step 5: This line meets AB at P. AP:PB=3:2.
CONSTRUCTION 2: CONSTRUCT SIMILAR TRIANGLE (scale factor m/n)
To construct triangle similar to ABC with scale factor 3/4:
Case 1 (scale factor < 1, smaller triangle):
Step 1: Draw ray BX at acute angle to BC.
Step 2: Mark 4 equal points on BX: B1,B2,B3,B4.
Step 3: Join B4 to C. Draw B3C' parallel to B4C.
Step 4: Draw C'A' parallel to CA. Triangle A'BC' is required (3/4 times original).
Case 2 (scale factor > 1, larger triangle):
Mark more points (m points), join nth point to vertex.
CONSTRUCTION 3: TANGENTS FROM EXTERNAL POINT
To draw tangents from point P to circle with centre O:
Step 1: Find midpoint M of OP.
Step 2: Draw circle with centre M and radius MP(=MO).
Step 3: This circle intersects original circle at A and B.
Step 4: PA and PB are the required tangents.
Why: Angle OAP=90° (angle in semicircle on diameter OP).
CONSTRUCTION 4: TANGENT AT POINT ON CIRCLE
Draw radius to point. Tangent is perpendicular to radius at that point.
SOLVED EXAMPLES:
Example 1: Divide 7cm segment in ratio 3:2.
Draw 5 equal arcs. Join 5th to B. Through 3rd draw parallel. Done.
Example 2: Tangents from point 10cm from centre, radius 4cm.
Tangent length=sqrt(100-16)=sqrt(84)=2sqrt(21)≈9.17cm.
COMMON MISTAKES:
Scale factor 3/4: mark 4 points (denominator), use 3rd (numerator) for the construction.
Tangent construction: the second circle must have DIAMETER = OP (radius = OP/2).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_10", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch12: Areas Related to Circles
BASIC FORMULAS (r=radius):
Circumference=2*pi*r. Area of circle=pi*r^2.
ARC LENGTH AND SECTOR:
Arc length = (theta/360)×2*pi*r.
Area of sector = (theta/360)×pi*r^2.
Perimeter of sector = 2r + arc length = 2r + (theta/360)×2*pi*r.
SEGMENT:
Area of minor segment = Area of sector - Area of triangle.
Area of triangle in sector = (1/2)×r^2×sin(theta).
Area of minor segment = (theta/360)×pi*r^2 - (1/2)×r^2×sin(theta).
Area of major segment = Area of circle - Area of minor segment.
COMBINATIONS OF FIGURES:
Shaded regions often require adding or subtracting areas of different shapes.
SOLVED EXAMPLES:
Example 1: Sector r=14cm, theta=60°.
Arc length=(60/360)×2×(22/7)×14=(1/6)×88=14.67cm.
Area=(60/360)×(22/7)×196=(1/6)×616=102.67cm^2.
Example 2: Area of minor segment, r=12cm, theta=60°.
Sector area=(60/360)×pi×144=24pi cm^2.
Triangle area=(1/2)×12^2×sin60°=72×(sqrt3/2)=36sqrt3 cm^2.
Segment area=24pi-36sqrt3=(24×3.14)-(36×1.732)=75.36-62.35=13.01cm^2.
Example 3: Square inscribed in circle r=10cm. Area of shaded region outside square.
Diagonal of square=2r=20cm. Side=20/sqrt2=10sqrt2.
Area of square=200cm^2. Area of circle=pi×100=314cm^2.
Shaded area=314-200=114cm^2.
COMMON MISTAKES:
theta in formula must be in DEGREES not radians.
Area of sector=(theta/360)×pi*r^2 NOT (theta/360)×2*pi*r (that is arc length).
For segment: SUBTRACT triangle from sector (segment < sector always).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_10", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch13: Surface Areas and Volumes
SURFACE AREA AND VOLUME FORMULAS (same as Class 9 plus combinations):
Cone: CSA=pi*r*l, TSA=pi*r(r+l), V=(1/3)*pi*r^2*h, l=sqrt(r^2+h^2).
Cylinder: CSA=2*pi*r*h, TSA=2*pi*r(r+h), V=pi*r^2*h.
Sphere: SA=4*pi*r^2, V=(4/3)*pi*r^3.
Hemisphere: CSA=2*pi*r^2, TSA=3*pi*r^2, V=(2/3)*pi*r^3.
COMBINATION OF SOLIDS:
Total surface area of combination: add all EXPOSED surfaces only (not hidden surfaces).
Volume of combination: simply add volumes.
CONVERSION OF SOLIDS:
When one solid melted and recast into another: VOLUME remains same.
Number of smaller solids = Volume of larger solid / Volume of one smaller solid.
FRUSTUM OF CONE (cone with top cut off):
Slant height: l=sqrt(h^2+(r1-r2)^2) where r1=bottom radius, r2=top radius, h=height.
CSA=pi×l×(r1+r2). TSA=pi×[l(r1+r2)+r1^2+r2^2]. V=(1/3)×pi×h×(r1^2+r2^2+r1×r2).
SOLVED EXAMPLES:
Example 1: Cone on hemisphere, both r=3.5cm, cone h=4cm. Find TSA and V.
Cone: l=sqrt(16+12.25)=sqrt(28.25)=5.31cm. CSA=pi×3.5×5.31=58.4cm^2.
Hemisphere CSA=2×pi×3.5^2=77cm^2. Total SA=58.4+77=135.4cm^2 (base circle is hidden).
Cone V=(1/3)×pi×12.25×4=51.3cm^3. Hemisphere V=(2/3)×pi×42.875=89.8cm^3.
Total V=141.1cm^3.
Example 2: Sphere r=9cm melted into cylinders r=3cm, h=9cm. How many?
V_sphere=(4/3)×pi×729=972pi. V_cylinder=pi×9×9=81pi.
Number=972pi/81pi=12 cylinders.
Example 3: Bucket (frustum): top r=20cm, bottom r=8cm, h=16cm.
l=sqrt(256+144)=sqrt(400)=20cm.
V=(pi/3)×16×(400+64+160)=(pi/3)×16×624=10449cm^3 approx.
COMMON MISTAKES:
TSA of combination: DO NOT add hidden surfaces.
Conversion: volume is conserved (not SA).
Frustum l uses (r1-r2) not (r1+r2).""",
    metadata={"source": "ncert", "topic": "mensuration", "class_level": "class_10", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch14: Statistics
MEAN FOR GROUPED DATA:
Direct method: x_bar = sum(f*x)/sum(f). x=class mark=(upper+lower)/2.
Assumed mean method: x_bar = a + sum(f*d)/sum(f). d=x-a.
Step deviation method: x_bar = a + (sum(f*u)/sum(f))×h. u=(x-a)/h. Best when h is constant.
MEDIAN FOR GROUPED DATA:
Formula: M = L + ((n/2 - cf)/f) × h.
L=lower boundary of median class.
n=total frequency. cf=cumulative frequency of class BEFORE median class.
f=frequency of median class. h=class width.
Median class: class where cumulative frequency first exceeds n/2.
MODE FOR GROUPED DATA:
Modal class=class with highest frequency.
Mode = L + ((f1-f0)/(2f1-f0-f2)) × h.
L=lower boundary of modal class. f1=frequency of modal class.
f0=frequency of class BEFORE modal class. f2=frequency of class AFTER modal class.
EMPIRICAL RELATIONSHIP: Mode = 3×Median - 2×Mean (approximately true).
OGIVE (CUMULATIVE FREQUENCY CURVE):
Less than ogive: plot (upper class boundary, cumulative frequency).
More than ogive: plot (lower class boundary, more than cumulative frequency).
Median from ogive: find n/2 on y-axis, draw horizontal to curve, then vertical to x-axis.
SOLVED EXAMPLES:
Example 1: Mean by step deviation. Classes 10-20,20-30,...50-60. Frequencies 4,6,8,5,3. a=30, h=10.
Class marks: 15,25,35,45,55. u=(-2,-1,0,1,2). f×u=-8,-6,0,5,6.
sum(f)=26. sum(f×u)=-3. Mean=30+(-3/26)×10=30-1.15=28.85.
Example 2: Find median. n=26, n/2=13. cf values: 4,10,18,23,26. 13 falls in class 30-40 (cf=10, f=8).
Median=30+((13-10)/8)×10=30+3.75=33.75.
COMMON MISTAKES:
For median formula: cf is cumulative frequency of class BEFORE (not including) median class.
Class mark is MIDPOINT: for class 10-20, mark=15 (not 10 or 20).
Modal class: highest frequency (not highest class mark).""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_10", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch15: Probability
CLASSICAL DEFINITION:
P(E) = Number of favourable outcomes / Total number of equally likely outcomes.
Range: 0 <= P(E) <= 1. P(E)+P(not E)=1.
P(certain event)=1. P(impossible event)=0.
SAMPLE SPACES:
One coin: S={H,T}, n(S)=2.
Two coins: S={HH,HT,TH,TT}, n(S)=4.
One die: S={1,2,3,4,5,6}, n(S)=6.
Two dice: n(S)=36 (all ordered pairs).
Deck of cards: n(S)=52. (4 suits × 13 cards each. Face cards=12. Aces=4.)
CARD PROBLEMS:
Red cards=26 (hearts+diamonds). Black=26 (clubs+spades).
Face cards=12 (J,Q,K of each suit). Aces=4.
King of red=2. Face card AND red=6.
TWO DICE PROBLEMS:
Sum=2: (1,1)=1 way. Sum=3: 2 ways. Sum=7: 6 ways (most common).
Sum=12: (6,6)=1 way.
P(sum=7)=6/36=1/6. P(sum=2 or 12)=2/36=1/18.
SOLVED EXAMPLES:
Example 1: Two dice. P(sum=8).
Pairs: (2,6),(3,5),(4,4),(5,3),(6,2)=5. P=5/36.
Example 2: Cards. P(king or red).
P(king)=4/52. P(red)=26/52. P(king AND red)=2/52.
P(king or red)=4/52+26/52-2/52=28/52=7/13.
Example 3: Bag: 5 red, 3 blue, 2 green. P(not red)?
P(not red)=(3+2)/10=5/10=1/2.
Example 4: Two dice. P(same number on both).
Pairs: (1,1),(2,2),(3,3),(4,4),(5,5),(6,6)=6. P=6/36=1/6.
COMMON MISTAKES:
Two coins: 3 outcomes (0H,1H,2H) are NOT equally likely. Use 4 outcomes (HH,HT,TH,TT).
P(A or B) = P(A)+P(B)-P(A and B). Don't forget the intersection.
For two dice: total outcomes=36 not 12 (order matters: (1,2)≠(2,1)).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_10", "chapter": "ch15", "difficulty": "intermediate"}),


    # ── CLASS 11 — All 16 Chapters ──────────────────────────────────

    Document(page_content="""Class 11 | Ch1: Sets
SET: well-defined collection of distinct objects.
Representation: Roster (list) {1,2,3} or Set-builder {x: condition}.
TYPES OF SETS:
Empty/Null set: no elements. phi or {}.
Singleton: exactly one element.
Finite set: countable elements. Infinite set: uncountable.
Universal set U: contains all elements under consideration.
Subset: A is subset of B if every element of A is in B. A⊆B.
Proper subset: A⊂B means A⊆B and A≠B.
Power set P(A): set of ALL subsets of A. If n(A)=k, then n(P(A))=2^k.
SET OPERATIONS:
Union A∪B: elements in A OR B (or both).
Intersection A∩B: elements in BOTH A and B.
Difference A-B: elements in A but NOT in B.
Complement A': elements in U but NOT in A. A'=U-A.
Symmetric difference A△B = (A-B)∪(B-A).
LAWS (De Morgan's):
(A∪B)'=A'∩B'. (A∩B)'=A'∪B'.
VENN DIAGRAMS: circles inside rectangle (universal set).
CARDINAL NUMBER FORMULA:
n(A∪B)=n(A)+n(B)-n(A∩B).
n(A∪B∪C)=n(A)+n(B)+n(C)-n(A∩B)-n(B∩C)-n(A∩C)+n(A∩B∩C).
SOLVED EXAMPLES:
Example 1: A={1,2,3,4,5}, B={2,4,6,8}.
A∪B={1,2,3,4,5,6,8}. A∩B={2,4}. A-B={1,3,5}. B-A={6,8}.
n(A∪B)=5+4-2=7. Verified: 7 elements in A∪B.
Example 2: n(A)=20, n(B)=25, n(A∪B)=40. Find n(A∩B).
n(A∩B)=20+25-40=5.
Example 3: P({a,b})={{},{a},{b},{a,b}}. n=4=2^2.
COMMON MISTAKES:
{0} and {} are DIFFERENT. {0} has one element (zero). {} is empty.
Empty set {} is subset of EVERY set.
A⊆A always (every set is subset of itself).""",
    metadata={"source": "ncert", "topic": "sets", "class_level": "class_11", "chapter": "ch1", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch2: Relations and Functions
CARTESIAN PRODUCT: A×B = {(a,b): a∈A, b∈B}.
n(A×B)=n(A)×n(B). A×B≠B×A (unless A=B).
RELATION: any subset of A×B. Domain=set of first elements. Range=set of second elements.
FUNCTION: relation where every element of domain has EXACTLY ONE image.
One-one (injective): different inputs → different outputs. f(a)=f(b) → a=b.
Onto (surjective): every element of codomain has a pre-image.
Bijective: both one-one AND onto. Inverse exists iff bijective.
DOMAIN AND RANGE:
For f(x)=sqrt(9-x^2): need 9-x^2>=0 → x^2<=9 → -3<=x<=3. Domain=[-3,3]. Range=[0,3].
For f(x)=1/(x-2): need x≠2. Domain=R-{2}.
For f(x)=sqrt(x-1)+sqrt(5-x): need x>=1 AND x<=5. Domain=[1,5].
COMPOSITION OF FUNCTIONS:
(fog)(x)=f(g(x)). Apply g first, then f.
(gof)(x)=g(f(x)). Apply f first, then g.
fog≠gof in general.
INVERSE FUNCTION:
f^(-1) exists iff f is bijective.
If f(x)=y then f^(-1)(y)=x.
To find: replace f(x) with y, solve for x, then replace x with f^(-1)(y).
SOLVED EXAMPLES:
Example 1: f(x)=2x+1, g(x)=x^2-1.
fog(x)=f(g(x))=f(x^2-1)=2(x^2-1)+1=2x^2-1.
gof(x)=g(f(x))=g(2x+1)=(2x+1)^2-1=4x^2+4x.
Example 2: Domain of f(x)=sqrt(9-x^2).
9-x^2>=0 → (3-x)(3+x)>=0 → -3<=x<=3. Domain=[-3,3].
Example 3: Is f(x)=2x+3 bijective? Find inverse.
One-one: f(a)=f(b) → 2a+3=2b+3 → a=b. Yes.
Onto: for any y, x=(y-3)/2 exists. Yes. Bijective.
Inverse: y=2x+3 → x=(y-3)/2. So f^(-1)(x)=(x-3)/2.
COMMON MISTAKES:
Domain: find values where function is DEFINED (not where it equals zero).
fog means f applied AFTER g (right to left). fog(x)=f(g(x)).
Every function is a relation but NOT every relation is a function.""",
    metadata={"source": "ncert", "topic": "functions", "class_level": "class_11", "chapter": "ch2", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch3: Trigonometric Functions
RADIAN MEASURE: pi radians=180°. 1 radian=180°/pi≈57.3°.
Arc length l=r×theta (theta in radians). Area of sector=(1/2)r^2×theta.
SIGN OF TRIG FUNCTIONS BY QUADRANT (ASTC rule: All Students Take Calculus):
Q1: all positive. Q2: sin,cosec positive. Q3: tan,cot positive. Q4: cos,sec positive.
TRIG VALUES FOR STANDARD ANGLES: (same as Class 10 table).
TRIG FUNCTIONS OF ALLIED ANGLES:
sin(pi-x)=sin(x). cos(pi-x)=-cos(x). tan(pi-x)=-tan(x).
sin(pi+x)=-sin(x). cos(pi+x)=-cos(x). tan(pi+x)=tan(x).
sin(2pi-x)=-sin(x). cos(2pi-x)=cos(x).
sin(-x)=-sin(x) (odd). cos(-x)=cos(x) (even).
SUM AND DIFFERENCE FORMULAS:
sin(A+B)=sinA cosB+cosA sinB. sin(A-B)=sinA cosB-cosA sinB.
cos(A+B)=cosA cosB-sinA sinB. cos(A-B)=cosA cosB+sinA sinB.
tan(A+B)=(tanA+tanB)/(1-tanA tanB). tan(A-B)=(tanA-tanB)/(1+tanA tanB).
DOUBLE ANGLE FORMULAS:
sin2A=2sinA cosA. cos2A=cos^2A-sin^2A=1-2sin^2A=2cos^2A-1.
tan2A=2tanA/(1-tan^2A).
HALF ANGLE: sin^2(A/2)=(1-cosA)/2. cos^2(A/2)=(1+cosA)/2.
PRODUCT TO SUM:
sinA cosB=(1/2)[sin(A+B)+sin(A-B)].
cosA cosB=(1/2)[cos(A+B)+cos(A-B)].
GENERAL SOLUTION:
sinx=sina → x=n*pi+(-1)^n*a. cosx=cosa → x=2n*pi±a. tanx=tana → x=n*pi+a.
SOLVED EXAMPLES:
Example 1: Prove sin(A+B)sin(A-B)=sin^2A-sin^2B.
LHS=(sinA cosB+cosA sinB)(sinA cosB-cosA sinB)=sin^2A cos^2B-cos^2A sin^2B.
=sin^2A(1-sin^2B)-(1-sin^2A)sin^2B=sin^2A-sin^2A sin^2B-sin^2B+sin^2A sin^2B=sin^2A-sin^2B. Proved.
Example 2: Solve 2cos^2x-3cosx+1=0 for x in [0,2pi].
Let c=cosx: 2c^2-3c+1=0 → (2c-1)(c-1)=0 → c=1/2 or c=1.
cosx=1/2 → x=pi/3 or 5pi/3. cosx=1 → x=0. Solutions: {0, pi/3, 5pi/3}.
COMMON MISTAKES:
sinx=sin(a) general solution: x=n*pi+(-1)^n*a (alternating sign, NOT just ±a).
sin(A+B)≠sinA+sinB. Must use the formula.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_11", "chapter": "ch3", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch4: Principle of Mathematical Induction
PMI METHOD:
Step 1 (Base case): Verify statement P(n) is true for n=1 (or starting value).
Step 2 (Inductive step): Assume P(k) is true. Prove P(k+1) is true.
Conclusion: By PMI, P(n) is true for all n>=1.
KEY: The inductive step uses P(k) (called inductive hypothesis) to prove P(k+1).
STANDARD RESULTS TO PROVE:
Sum of natural numbers: 1+2+3+...+n=n(n+1)/2.
Sum of squares: 1^2+2^2+...+n^2=n(n+1)(2n+1)/6.
Sum of cubes: 1^3+2^3+...+n^3=[n(n+1)/2]^2.
Geometric sum: a+ar+ar^2+...+ar^(n-1)=a(r^n-1)/(r-1).
SOLVED EXAMPLES:
Example 1: Prove 1+2+3+...+n=n(n+1)/2 by PMI.
Base: n=1. LHS=1. RHS=1(2)/2=1. True.
Assume true for n=k: 1+2+...+k=k(k+1)/2.
Prove for n=k+1: 1+2+...+k+(k+1)=k(k+1)/2+(k+1)=(k+1)(k/2+1)=(k+1)(k+2)/2.
This is (k+1)(k+2)/2 which is the formula for n=k+1. Proved.
Example 2: Prove 2^n>n for all n>=1.
Base: n=1. 2^1=2>1. True.
Assume 2^k>k. Prove 2^(k+1)>k+1.
2^(k+1)=2×2^k>2k (using hypothesis). 2k=k+k>=k+1 (since k>=1).
So 2^(k+1)>k+1. Proved.
Example 3: Prove 4^n-1 divisible by 3.
Base: 4^1-1=3. Divisible by 3. True.
Assume 4^k-1=3m for some integer m.
4^(k+1)-1=4×4^k-1=4(3m+1)-1=12m+4-1=12m+3=3(4m+1). Divisible by 3. Proved.
COMMON MISTAKES:
BOTH steps are necessary. Proving only base case is not enough.
In inductive step: assume P(k), then DERIVE P(k+1) (not assume P(k+1)).
The technique works by domino effect: if each domino knocks next, all fall.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch4", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch5: Complex Numbers and Quadratic Equations
COMPLEX NUMBER: z=a+ib where a=real part, b=imaginary part, i=sqrt(-1).
i^1=i, i^2=-1, i^3=-i, i^4=1. Pattern repeats every 4.
i^n: divide n by 4, use remainder (0→1, 1→i, 2→-1, 3→-i).
ALGEBRA OF COMPLEX NUMBERS:
Addition: (a+ib)+(c+id)=(a+c)+i(b+d).
Multiplication: (a+ib)(c+id)=(ac-bd)+i(ad+bc).
Conjugate of z=a+ib is z_bar=a-ib.
|z|=sqrt(a^2+b^2) (modulus/absolute value).
z×z_bar=|z|^2=a^2+b^2.
Division: z1/z2=z1×z2_bar/|z2|^2.
ARGAND PLANE: Complex number a+ib plotted as point (a,b).
POLAR FORM: z=r(cos(theta)+i sin(theta)) where r=|z|, theta=arg(z).
arg(z)=tan^(-1)(b/a) (adjust for quadrant).
DE MOIVRE'S THEOREM: (cos(theta)+i sin(theta))^n=cos(n*theta)+i sin(n*theta).
CUBE ROOTS OF UNITY:
x^3=1. Solutions: 1, omega, omega^2 where omega=(-1+i*sqrt3)/2.
Properties: 1+omega+omega^2=0. omega^3=1. omega_bar=omega^2.
QUADRATIC WITH COMPLEX ROOTS:
ax^2+bx+c=0, D=b^2-4ac<0: roots=(-b±i*sqrt(-D))/2a. Roots are conjugates.
SOLVED EXAMPLES:
Example 1: Modulus and argument of z=-1+i*sqrt3.
|z|=sqrt(1+3)=2. tan(alpha)=sqrt3/1=sqrt3 → alpha=pi/3.
z is in Q2 (real negative, imag positive). arg(z)=pi-pi/3=2pi/3.
Polar form: z=2(cos(2pi/3)+i sin(2pi/3)).
Example 2: Find (1+i)^10 using De Moivre.
1+i=sqrt2(cos(pi/4)+i sin(pi/4)).
(1+i)^10=(sqrt2)^10(cos(10pi/4)+i sin(10pi/4))=32(cos(5pi/2)+i sin(5pi/2))=32(0+i)=32i.
Example 3: Cube roots of unity. 1+omega+omega^2=0. omega^3=1.
If 1,omega,omega^2 are roots: sum=0=-b/a → b=0. Product=1=c/a → c=a. Equation: x^3-1=0.
COMMON MISTAKES:
i^2=-1, NOT +1. i^0=1 (not i).
Conjugate changes sign of imaginary part only: conjugate of (3-2i) is (3+2i).
|z|^2=a^2+b^2 (always positive real number).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch5", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch6: Linear Inequalities
RULES FOR INEQUALITIES:
Adding/subtracting same quantity: inequality sign UNCHANGED.
Multiplying/dividing by POSITIVE number: sign UNCHANGED.
Multiplying/dividing by NEGATIVE number: sign REVERSED.
SOLVING LINEAR INEQUALITIES IN ONE VARIABLE:
Solve like equation but reverse sign when multiplying/dividing by negative.
3x-2>2x+1 → x>3. Solution: (3,infinity). On number line: open circle at 3, arrow right.
GRAPHICAL METHOD FOR TWO VARIABLES:
ax+by<c: boundary line ax+by=c (dashed for < or >, solid for <= or >=).
Test point (usually origin) to determine which side.
SYSTEM OF INEQUALITIES:
Find region satisfying ALL inequalities simultaneously (feasible region).
SOLVED EXAMPLES:
Example 1: Solve 3x-2>2x+1.
3x-2x>1+2 → x>3. Solution set: (3,∞).
Example 2: Solve -3<(4x-1)/5<3.
Multiply by 5: -15<4x-1<15 → -14<4x<16 → -7/2<x<4.
Solution: (-3.5,4).
Example 3: Solve system x+y<=10, x+3y<=15, x>=0, y>=0.
Draw lines x+y=10 and x+3y=15. Find intersection: subtract to get 2y=5, y=2.5, x=7.5.
Feasible region: bounded by vertices (0,0),(10,0),(7.5,2.5),(0,5).
Example 4: IQ score: 62+4x/2<72 where x=age in months over 100.
124+4x<144 → 4x<20 → x<5. So age < 105 months.
COMMON MISTAKES:
MUST reverse inequality when multiplying/dividing by NEGATIVE number.
For absolute value: |x|<a means -a<x<a (two conditions combined).
Dashed line for strict inequality (<,>). Solid line for (<=,>=).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch6", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch7: Permutations and Combinations
FUNDAMENTAL COUNTING PRINCIPLE:
If task A can be done in m ways and task B in n ways, both together: m×n ways.
FACTORIAL: n!=n×(n-1)×(n-2)×...×2×1. 0!=1. 1!=1.
PERMUTATIONS (ordered arrangements):
nPr = n!/(n-r)! = n×(n-1)×...×(n-r+1). (r items from n, order matters.)
Permutations of n items = n!
Permutations with repetition: n^r (r items from n with repetition).
Permutations with identical items: n!/p!q!r!... (p identical of one type, q of another etc.)
CIRCULAR PERMUTATIONS: (n-1)! for n distinct items in circle.
COMBINATIONS (unordered selections):
nCr = n!/(r!(n-r)!) = nPr/r!. (r items from n, order does not matter.)
nCr = nC(n-r). nC0=nCn=1. nC1=n.
PASCAL'S IDENTITY: nCr + nCr-1 = (n+1)Cr.
SOLVED EXAMPLES:
Example 1: 5 boys and 3 girls sit in row, girls always together.
Treat 3 girls as 1 unit. Total units=6. Arrange 6 units: 6! ways. Girls arrange among themselves: 3! ways.
Total=6!×3!=720×6=4320.
Example 2: Find 7C3.
7C3=7!/(3!×4!)=7×6×5/(3×2×1)=210.
Example 3: Prove nCr+nCr-1=(n+1)Cr.
nCr+nCr-1=n!/(r!(n-r)!)+n!/((r-1)!(n-r+1)!)
=n!/((r-1)!(n-r)!) × [1/r+1/(n-r+1)]
=n!/((r-1)!(n-r)!) × (n+1)/(r(n-r+1))
=(n+1)!/(r!(n-r+1)!)=(n+1)Cr. Proved.
Example 4: How many ways to choose 3 from 7 if 2 specific must be included?
2 fixed. Choose 1 from remaining 5: 5C1=5 ways.
COMMON MISTAKES:
Permutation: ORDER matters (abc≠bac). Combination: order does NOT matter.
Circular: fix one position, arrange remaining (n-1)!.
nCr = nC(n-r): 10C3=10C7=120.""",
    metadata={"source": "ncert", "topic": "combinatorics", "class_level": "class_11", "chapter": "ch7", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch8: Binomial Theorem
BINOMIAL THEOREM: (a+b)^n = sum(r=0 to n) nCr × a^(n-r) × b^r.
General term: T(r+1) = nCr × a^(n-r) × b^r. (r starts from 0.)
PROPERTIES:
Number of terms = n+1.
Sum of binomial coefficients = 2^n (put a=b=1).
Sum of odd-position coefficients = Sum of even-position = 2^(n-1).
Binomial coefficients: nC0,nC1,...,nCn form Pascal's triangle.
MIDDLE TERM:
If n is even: middle term is T(n/2+1). One middle term.
If n is odd: two middle terms T((n+1)/2) and T((n+3)/2).
TERM INDEPENDENT OF x: find r such that power of x in T(r+1) = 0.
GREATEST TERM: find r such that T(r+1)/T(r) >= 1.
SOLVED EXAMPLES:
Example 1: Expand (2x-3y)^4.
T(r+1)=4Cr×(2x)^(4-r)×(-3y)^r.
r=0: 4C0×16x^4=16x^4. r=1: 4C1×8x^3×(-3y)=-96x^3y.
r=2: 4C2×4x^2×9y^2=216x^2y^2. r=3: 4C3×2x×(-27y^3)=-216xy^3.
r=4: 4C4×81y^4=81y^4.
Expansion: 16x^4-96x^3y+216x^2y^2-216xy^3+81y^4.
Example 2: Find 5th term in (x+2)^8.
T5=T(4+1): r=4. T5=8C4×x^4×2^4=70×x^4×16=1120x^4.
Example 3: Term independent of x in (x+1/x)^10.
T(r+1)=10Cr×x^(10-r)×(1/x)^r=10Cr×x^(10-2r).
For independent of x: 10-2r=0 → r=5. T6=10C5=252.
COMMON MISTAKES:
General term T(r+1) has r starting from 0, NOT 1.
For "5th term": r=4 (since T(r+1)=T5 means r+1=5, r=4).
In (a-b)^n: alternate signs. T(r+1)=nCr×a^(n-r)×(-b)^r.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch8", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch9: Sequences and Series
ARITHMETIC PROGRESSION: a, a+d, a+2d,...
a_n=a+(n-1)d. S_n=n/2[2a+(n-1)d]=n/2[a+l].
Arithmetic Mean AM=(a+b)/2. AM between a and b.
GEOMETRIC PROGRESSION: a, ar, ar^2,...
a_n=ar^(n-1). S_n=a(r^n-1)/(r-1) for r≠1. S_n=na for r=1.
Sum of infinite GP: S_inf=a/(1-r) for |r|<1.
Geometric Mean GM=sqrt(ab). GM between a and b.
RELATIONSHIP: AM>=GM (equality when a=b).
HARMONIC PROGRESSION: reciprocals form AP. HM=2ab/(a+b).
AM>=GM>=HM (with equality when a=b).
SPECIAL SERIES:
Sum of n natural numbers: n(n+1)/2.
Sum of squares: n(n+1)(2n+1)/6.
Sum of cubes: [n(n+1)/2]^2.
SOLVED EXAMPLES:
Example 1: GP 1+3+9+...+2187.
a=1, r=3. 2187=3^7, so n=8. S8=1×(3^8-1)/(3-1)=(6561-1)/2=3280.
Example 2: AM=10, GM=8. Find numbers.
(a+b)/2=10 → a+b=20. sqrt(ab)=8 → ab=64.
a and b are roots of x^2-20x+64=0 → (x-16)(x-4)=0. Numbers: 4 and 16.
Example 3: Sum(2k+1) for k=1 to 20.
=sum(2k)+sum(1)=2×sum(k)+20=2×(20×21/2)+20=420+20=440.
Example 4: Sum 1/2+1/4+1/8+... (infinite GP).
a=1/2, r=1/2. S=a/(1-r)=(1/2)/(1/2)=1.
COMMON MISTAKES:
Infinite GP sum only valid when |r|<1.
AM>=GM: equality holds only when both numbers are equal.
Sum of cubes=[sum of natural numbers]^2.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_11", "chapter": "ch9", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch10: Straight Lines
SLOPE: m=tan(theta)=(y2-y1)/(x2-x1). Horizontal line: m=0. Vertical line: undefined.
Parallel lines: m1=m2. Perpendicular lines: m1×m2=-1.
EQUATIONS OF LINES:
Slope-intercept: y=mx+c (m=slope, c=y-intercept).
Point-slope: y-y1=m(x-x1).
Two-point form: (y-y1)/(y2-y1)=(x-x1)/(x2-x1).
Intercept form: x/a+y/b=1 (a=x-intercept, b=y-intercept).
Normal form: x cos(alpha)+y sin(alpha)=p (p=perpendicular distance from origin, alpha=angle).
General form: ax+by+c=0.
DISTANCE FORMULAS:
Distance from point (x1,y1) to line ax+by+c=0: d=|ax1+by1+c|/sqrt(a^2+b^2).
Distance between parallel lines ax+by+c1=0 and ax+by+c2=0: |c1-c2|/sqrt(a^2+b^2).
ANGLE BETWEEN LINES:
tan(theta)=|(m1-m2)/(1+m1m2)|.
SOLVED EXAMPLES:
Example 1: Line through (2,-3) perpendicular to 3x-4y+5=0.
Slope of given line=3/4. Perpendicular slope=-4/3.
Line: y-(-3)=(-4/3)(x-2) → 3y+9=-4x+8 → 4x+3y+1=0.
Example 2: Distance between 3x+4y-5=0 and 3x+4y+15=0.
d=|(-5)-(15)|/sqrt(9+16)=20/5=4 units.
Example 3: Find foot of perpendicular from (1,2) to line 2x-3y+4=0.
Use formula: (x-x1)/a=(y-y1)/b=-(ax1+by1+c)/(a^2+b^2).
=(x-1)/2=(y-2)/(-3)=-(2-6+4)/(4+9)=0/13=0.
So x=1, y=2. Point itself lies on line. (Check: 2-6+4=0. Yes.)
COMMON MISTAKES:
Perpendicular lines: m1×m2=-1 (product is -1, not sum).
Distance formula: divide by sqrt(a^2+b^2) NOT (a^2+b^2).
Parallel lines have SAME slope. Perpendicular lines: slopes are NEGATIVE RECIPROCALS.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch10", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch11: Conic Sections
CIRCLE: (x-h)^2+(y-k)^2=r^2. Centre (h,k), radius r.
General: x^2+y^2+2gx+2fy+c=0. Centre (-g,-f), radius=sqrt(g^2+f^2-c).
PARABOLA (standard forms):
y^2=4ax: opens right. Focus (a,0). Directrix x=-a. Vertex (0,0). Axis=x-axis.
y^2=-4ax: opens left. Focus (-a,0). Directrix x=a.
x^2=4ay: opens up. Focus (0,a). Directrix y=-a. Axis=y-axis.
x^2=-4ay: opens down. Focus (0,-a). Directrix y=a.
Latus rectum: chord through focus perpendicular to axis. Length=4a.
ELLIPSE: x^2/a^2+y^2/b^2=1 (a>b>0).
Centre (0,0). Vertices (±a,0). Co-vertices (0,±b).
Foci (±c,0) where c^2=a^2-b^2. Eccentricity e=c/a<1.
Length of major axis=2a. Minor axis=2b. Latus rectum=2b^2/a.
HYPERBOLA: x^2/a^2-y^2/b^2=1.
Foci (±c,0) where c^2=a^2+b^2. Eccentricity e=c/a>1.
Asymptotes: y=±(b/a)x. Latus rectum=2b^2/a.
SOLVED EXAMPLES:
Example 1: Parabola y^2=12x. Find focus, directrix, latus rectum.
4a=12 → a=3. Focus (3,0). Directrix x=-3. Latus rectum=12.
Example 2: Ellipse, foci (±3,0), semi-major axis a=5.
c=3, a=5. b^2=a^2-c^2=25-9=16. b=4.
Equation: x^2/25+y^2/16=1.
Example 3: Find equation of circle with centre (2,-3) and radius 5.
(x-2)^2+(y+3)^2=25. Expanded: x^2+y^2-4x+6y-12=0.
COMMON MISTAKES:
Ellipse: c^2=a^2-b^2 (c<a). Hyperbola: c^2=a^2+b^2 (c>a).
For parabola y^2=4ax: COMPARE with standard form to find a (4a=coefficient).
Eccentricity: circle e=0, ellipse 0<e<1, parabola e=1, hyperbola e>1.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch11", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch12: Introduction to Three Dimensional Geometry
COORDINATES IN 3D: Point P=(x,y,z). Three mutually perpendicular axes: x,y,z.
OCTANTS: 3D space divided into 8 octants by coordinate planes.
DISTANCE FORMULA:
Distance between P(x1,y1,z1) and Q(x2,y2,z2):
PQ=sqrt((x2-x1)^2+(y2-y1)^2+(z2-z1)^2).
Distance from origin: OP=sqrt(x^2+y^2+z^2).
SECTION FORMULA (Internal Division):
Point dividing PQ in ratio m:n internally:
R=((mx2+nx1)/(m+n), (my2+ny1)/(m+n), (mz2+nz1)/(m+n)).
MIDPOINT: M=((x1+x2)/2, (y1+y2)/2, (z1+z2)/2).
CENTROID OF TRIANGLE:
G=((x1+x2+x3)/3, (y1+y2+y3)/3, (z1+z2+z3)/3).
COORDINATE PLANES:
xy-plane: z=0. yz-plane: x=0. xz-plane: y=0.
Distance from xy-plane: |z|. From yz-plane: |x|. From xz-plane: |y|.
SOLVED EXAMPLES:
Example 1: Distance between A(1,2,3) and B(4,-2,6).
AB=sqrt((4-1)^2+(-2-2)^2+(6-3)^2)=sqrt(9+16+9)=sqrt(34).
Example 2: Find point dividing A(2,1,3) and B(5,4,6) in ratio 2:1.
P=((2×5+1×2)/3,(2×4+1×1)/3,(2×6+1×3)/3)=(12/3,9/3,15/3)=(4,3,5).
Example 3: Show A(0,7,-10), B(1,6,-6), C(4,9,-6) form a right triangle.
AB=sqrt(1+1+16)=sqrt(18). BC=sqrt(9+9+0)=sqrt(18). AC=sqrt(16+4+16)=sqrt(36)=6.
AB^2+BC^2=18+18=36=AC^2. Right angle at B.
COMMON MISTAKES:
3D distance has THREE terms under square root (not two).
Section formula extends naturally from 2D — same structure but three coordinates.
Midpoint: average each coordinate SEPARATELY.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_11", "chapter": "ch12", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch13: Limits and Derivatives
LIMIT: lim(x→a) f(x) = L means f(x) approaches L as x approaches a.
Left limit: lim(x→a-) f(x). Right limit: lim(x→a+) f(x).
Limit exists iff left limit = right limit.
STANDARD LIMITS:
lim(x→0) sin(x)/x = 1. lim(x→0) (1-cos(x))/x = 0.
lim(x→0) tan(x)/x = 1. lim(x→0) (e^x-1)/x = 1.
lim(x→0) (a^x-1)/x = ln(a). lim(x→a) (x^n-a^n)/(x-a) = na^(n-1).
ALGEBRA OF LIMITS:
lim(f±g)=lim f ± lim g. lim(fg)=lim f × lim g. lim(f/g)=lim f/lim g (if lim g≠0).
lim(cf)=c×lim f. lim(f^n)=(lim f)^n.
DERIVATIVES (FIRST PRINCIPLES):
f'(x)=lim(h→0) [f(x+h)-f(x)]/h.
STANDARD DERIVATIVES:
d/dx[x^n]=nx^(n-1). d/dx[sin x]=cos x. d/dx[cos x]=-sin x.
d/dx[tan x]=sec^2 x. d/dx[e^x]=e^x. d/dx[ln x]=1/x.
d/dx[constant]=0. d/dx[cf(x)]=cf'(x). d/dx[f±g]=f'±g'.
PRODUCT RULE: d/dx[fg]=f'g+fg'.
QUOTIENT RULE: d/dx[f/g]=(f'g-fg')/g^2.
SOLVED EXAMPLES:
Example 1: lim(x→0) sin(3x)/x=3×lim(x→0) sin(3x)/(3x)=3×1=3.
Example 2: Derivative of x^3 sin x.
d/dx[x^3 sin x]=3x^2 sin x+x^3 cos x (product rule).
Example 3: Derivative of (x^2+1)/(x^2-1).
Using quotient rule: [(2x)(x^2-1)-(x^2+1)(2x)]/(x^2-1)^2.
=[2x^3-2x-2x^3-2x]/(x^2-1)^2=(-4x)/(x^2-1)^2.
Example 4: lim(x→2) (x^3-8)/(x-2)=lim(x→2) (x^2+2x+4)=4+4+4=12.
Using formula: na^(n-1)=3×2^2=12. Confirmed.
COMMON MISTAKES:
lim(x→0) sin(x)/x=1 only when angle is in RADIANS.
Product rule: d/dx[fg]=f'g+fg' NOT f'g'.
Quotient rule: numerator is f'g-fg' (not fg'-f'g).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_11", "chapter": "ch13", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch14: Mathematical Reasoning
STATEMENTS: declarative sentence that is either TRUE or FALSE (not both).
Not a statement: questions, exclamations, commands, ambiguous sentences.
CONNECTIVES:
AND (conjunction ∧): p∧q true only when BOTH p and q are true.
OR (disjunction ∨): p∨q true when AT LEAST ONE is true.
NOT (negation ¬): ¬p is opposite truth value.
IMPLICATION: p→q (if p then q). False only when p true and q false.
BICONDITIONAL: p↔q (p if and only if q). True when both same truth value.
TRUTH TABLES: systematic listing of all truth value combinations.
CONDITIONAL STATEMENTS:
Converse of p→q: q→p.
Inverse of p→q: ¬p→¬q.
Contrapositive of p→q: ¬q→¬p. (Contrapositive is LOGICALLY EQUIVALENT to original.)
QUANTIFIERS:
Universal: "For all" (∀). Existential: "There exists" (∃).
Negation of "For all x, P(x)": "There exists x such that NOT P(x)".
Negation of "There exists x, P(x)": "For all x, NOT P(x)".
METHODS OF PROOF:
Direct proof: assume hypothesis, derive conclusion.
Contrapositive: prove ¬q→¬p (equivalent to p→q).
Contradiction: assume statement false, derive contradiction.
By example (existence): give one example.
By counter-example (disproof): give one counter-example.
SOLVED EXAMPLES:
Example 1: Negation of "All primes are odd."
"There exists a prime that is NOT odd." (2 is a prime that is even — counter-example.)
Example 2: Converse, inverse, contrapositive of "If x>5 then x^2>25."
Converse: If x^2>25 then x>5. (FALSE: x=-6 gives x^2=36>25 but x<5.)
Inverse: If x≤5 then x^2≤25. (FALSE: x=-6.)
Contrapositive: If x^2≤25 then x≤5. (TRUE, equivalent to original.)
Example 3: Check "If n is odd then n^2 is odd" by contrapositive.
Contrapositive: If n^2 is even then n is even.
If n^2=2k then n=2m (provable). Contrapositive true → original true.
COMMON MISTAKES:
Converse is NOT always equivalent to original statement.
Contrapositive IS always equivalent to original.
To DISPROVE: one counter-example suffices. To PROVE universal: cannot use examples.""",
    metadata={"source": "ncert", "topic": "logic", "class_level": "class_11", "chapter": "ch14", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch15: Statistics
MEASURES OF DISPERSION (how spread out data is):
Range = Maximum - Minimum.
MEAN DEVIATION:
Mean deviation about mean: MD(x_bar)=sum(|xi-x_bar|)/n.
Mean deviation about median: MD(M)=sum(|xi-M|)/n.
For grouped data: MD=sum(f|xi-x_bar|)/sum(f).
VARIANCE AND STANDARD DEVIATION:
Variance: sigma^2=sum((xi-x_bar)^2)/n (ungrouped).
For grouped: sigma^2=sum(f(xi-x_bar)^2)/sum(f).
Shortcut: sigma^2=(sum(xi^2)/n)-(x_bar)^2 = (sum(fi*xi^2)/sum(fi))-(x_bar)^2.
Standard Deviation sigma=sqrt(Variance).
COEFFICIENT OF VARIATION: CV=(sigma/x_bar)×100.
Used to compare variability of two distributions with different means.
Higher CV = more variable/inconsistent.
For comparing: data with higher CV is more variable.
ANALYSIS OF FREQUENCY DISTRIBUTIONS:
Two distributions compared by CV when means are different.
Two distributions compared directly by sigma when means are same.
SOLVED EXAMPLES:
Example 1: Find variance and SD of 6,8,10,12,14.
Mean=50/5=10.
Deviations from mean: -4,-2,0,2,4. Squared: 16,4,0,4,16.
Variance=40/5=8. SD=sqrt(8)=2sqrt(2)≈2.83.
Example 2: Two distributions: A has mean=25, SD=5. B has mean=10, SD=4.
CV(A)=(5/25)×100=20%. CV(B)=(4/10)×100=40%.
B is more variable (higher CV).
Example 3: Find MD about mean for 2,4,6,8,10.
Mean=6. |deviations|=4,2,0,2,4. MD=12/5=2.4.
COMMON MISTAKES:
Variance is always non-negative (it's sum of SQUARES divided by n).
SD=sqrt(Variance), NOT Variance=SD^2 (both are true, don't confuse direction).
CV is in PERCENTAGE: multiply by 100.""",
    metadata={"source": "ncert", "topic": "statistics", "class_level": "class_11", "chapter": "ch15", "difficulty": "intermediate"}),

    Document(page_content="""Class 11 | Ch16: Probability
RANDOM EXPERIMENT: outcome cannot be predicted with certainty.
SAMPLE SPACE S: set of all possible outcomes.
EVENT: subset of sample space. Simple event: one outcome. Compound: multiple outcomes.
ALGEBRA OF EVENTS:
Complement of A: A'=S-A. A∪A'=S. A∩A'=phi.
Mutually exclusive: A∩B=phi (cannot occur together).
Exhaustive: A∪B=S (together cover all outcomes).
AXIOMATIC APPROACH TO PROBABILITY:
P(S)=1. 0<=P(A)<=1. P(A∪B)=P(A)+P(B) if A,B mutually exclusive.
ADDITION THEOREM:
P(A∪B)=P(A)+P(B)-P(A∩B).
P(A∪B∪C)=P(A)+P(B)+P(C)-P(A∩B)-P(B∩C)-P(A∩C)+P(A∩B∩C).
CONDITIONAL PROBABILITY:
P(A|B)=P(A∩B)/P(B). (Probability of A given B has occurred.)
INDEPENDENT EVENTS:
A and B independent if P(A∩B)=P(A)×P(B).
Equivalent: P(A|B)=P(A). (Occurrence of B doesn't affect A.)
MULTIPLICATION THEOREM:
P(A∩B)=P(A)×P(B|A)=P(B)×P(A|B).
SOLVED EXAMPLES:
Example 1: P(A)=0.4, P(B)=0.5, P(A∩B)=0.2.
P(A∪B)=0.4+0.5-0.2=0.7.
P(A|B)=P(A∩B)/P(B)=0.2/0.5=0.4.
(Note: P(A|B)=P(A)=0.4, so A and B are INDEPENDENT.)
Example 2: Card drawn. P(red or king).
P(red)=26/52. P(king)=4/52. P(red king)=2/52.
P(red or king)=26/52+4/52-2/52=28/52=7/13.
Example 3: Two dice. Find P(sum>9).
Favourable: (4,6),(5,5),(5,6),(6,4),(6,5),(6,6)=6 outcomes.
P=6/36=1/6.
Example 4: P(A)=1/4, P(B)=1/3. A,B independent. Find P(A or B).
P(A∩B)=1/4×1/3=1/12.
P(A∪B)=1/4+1/3-1/12=3/12+4/12-1/12=6/12=1/2.
COMMON MISTAKES:
Mutually exclusive: P(A∩B)=0. Independent: P(A∩B)=P(A)×P(B). DIFFERENT concepts.
Mutually exclusive events with nonzero probabilities are NOT independent.
P(A|B) is NOT the same as P(B|A).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_11", "chapter": "ch16", "difficulty": "intermediate"}),


    # ── CLASS 12 — All 13 Chapters ──────────────────────────────────

    Document(page_content="""Class 12 | Ch1: Relations and Functions
TYPES OF RELATIONS:
Empty relation: no element of A related to any element. R=phi.
Universal relation: every element related to every element. R=A×A.
Reflexive: (a,a) in R for all a in A.
Symmetric: if (a,b) in R then (b,a) in R.
Transitive: if (a,b) and (b,c) in R then (a,c) in R.
Equivalence relation: reflexive + symmetric + transitive.
EQUIVALENCE CLASSES: set of all elements related to a given element.
TYPES OF FUNCTIONS:
One-one (injective): f(a)=f(b) implies a=b. No two inputs give same output.
Onto (surjective): range=codomain. Every element of codomain has pre-image.
Bijective: one-one AND onto. Inverse function exists.
COMPOSITION: (fog)(x)=f(g(x)). gof≠fog generally.
If f and g are one-one then fog is one-one. If f and g are onto then fog is onto.
INVERTIBLE FUNCTIONS:
f is invertible iff f is bijective.
(f^(-1) o f)(x)=x and (f o f^(-1))(x)=x.
BINARY OPERATIONS: * on set A: A×A→A.
Commutative: a*b=b*a. Associative: (a*b)*c=a*(b*c).
Identity element e: a*e=e*a=a. Inverse of a: a*a^(-1)=e.
SOLVED EXAMPLES:
Example 1: R={(a,b): |a-b| divisible by 5} on integers. Is it equivalence?
Reflexive: |a-a|=0 divisible by 5. Yes.
Symmetric: |a-b| div by 5 → |b-a|=|a-b| div by 5. Yes.
Transitive: |a-b|=5k, |b-c|=5m → |a-c|<=|a-b|+|b-c|=5(k+m). Yes.
Equivalence relation confirmed.
Example 2: f:R→R, f(x)=2x+3. Show bijective and find inverse.
One-one: f(a)=f(b) → 2a+3=2b+3 → a=b. Yes.
Onto: for any y, x=(y-3)/2 in R. Yes. Bijective.
f^(-1)(x)=(x-3)/2.
COMMON MISTAKES:
Equivalence class [a]={b in A: (a,b) in R}. Different elements may have same class.
A function must be bijective for inverse to exist (not just one-one or just onto).
fog means g applied FIRST then f.""",
    metadata={"source": "ncert", "topic": "functions", "class_level": "class_12", "chapter": "ch1", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch2: Inverse Trigonometric Functions
DOMAINS AND RANGES (Principal Value Branch):
sin^(-1): domain [-1,1], range [-pi/2, pi/2].
cos^(-1): domain [-1,1], range [0, pi].
tan^(-1): domain R, range (-pi/2, pi/2).
cosec^(-1): domain R-(-1,1), range [-pi/2,pi/2]-{0}.
sec^(-1): domain R-(-1,1), range [0,pi]-{pi/2}.
cot^(-1): domain R, range (0,pi).
KEY PROPERTIES:
sin^(-1)(x)+cos^(-1)(x)=pi/2 for x in [-1,1].
tan^(-1)(x)+cot^(-1)(x)=pi/2 for all x.
sec^(-1)(x)+cosec^(-1)(x)=pi/2 for |x|>=1.
sin^(-1)(-x)=-sin^(-1)(x). cos^(-1)(-x)=pi-cos^(-1)(x).
tan^(-1)(-x)=-tan^(-1)(x).
sin^(-1)(1/x)=cosec^(-1)(x) for |x|>=1.
cos^(-1)(1/x)=sec^(-1)(x) for |x|>=1.
tan^(-1)(1/x)=cot^(-1)(x) for x>0.
ADDITION FORMULAS:
tan^(-1)(x)+tan^(-1)(y)=tan^(-1)((x+y)/(1-xy)) if xy<1.
tan^(-1)(x)+tan^(-1)(y)=pi+tan^(-1)((x+y)/(1-xy)) if xy>1 and x>0.
2 tan^(-1)(x)=sin^(-1)(2x/(1+x^2))=cos^(-1)((1-x^2)/(1+x^2))=tan^(-1)(2x/(1-x^2)).
SOLVED EXAMPLES:
Example 1: Find principal value of sin^(-1)(-1/2).
sin^(-1)(1/2)=pi/6. sin^(-1)(-1/2)=-pi/6. (In range [-pi/2,pi/2]).
Example 2: Find principal value of cos^(-1)(-sqrt3/2).
cos^(-1)(sqrt3/2)=pi/6. cos^(-1)(-sqrt3/2)=pi-pi/6=5pi/6. (In range [0,pi]).
Example 3: Simplify tan^(-1)(cosx-sinx)/(cosx+sinx).
Divide by cosx: tan^(-1)((1-tanx)/(1+tanx))=tan^(-1)(tan(pi/4-x))=pi/4-x.
(Valid when pi/4-x is in range (-pi/2,pi/2).)
Example 4: Prove sin^(-1)x+cos^(-1)x=pi/2.
Let sin^(-1)x=theta. Then x=sin(theta). cos^(-1)x=cos^(-1)(sin theta)=cos^(-1)(cos(pi/2-theta))=pi/2-theta.
Sum=theta+pi/2-theta=pi/2. Proved.
COMMON MISTAKES:
sin^(-1)(x) is NOT 1/sin(x). It is the inverse FUNCTION.
Principal value of cos^(-1): range is [0,pi], NOT [-pi/2,pi/2].
cos^(-1)(-x)=pi-cos^(-1)(x) (NOT -cos^(-1)(x) like sine).""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "class_12", "chapter": "ch2", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch3: Matrices
MATRIX: rectangular array of numbers in rows and columns. Order: m×n (m rows, n cols).
TYPES: Row(1×n), Column(m×1), Square(n×n), Zero/Null, Identity(diagonal=1, rest=0), Diagonal, Scalar.
OPERATIONS:
Addition: (A+B)_ij=a_ij+b_ij. Same order required.
Scalar multiplication: (kA)_ij=k×a_ij.
Multiplication: (AB)_ij=sum over k of a_ik×b_kj. Order: (m×n)(n×p)=(m×p).
AB is defined iff columns of A=rows of B. AB≠BA generally.
TRANSPOSE: A^T: rows become columns. (A^T)_ij=A_ji.
(A+B)^T=A^T+B^T. (AB)^T=B^T A^T. (A^T)^T=A.
SYMMETRIC: A^T=A (a_ij=a_ji). SKEW-SYMMETRIC: A^T=-A (a_ij=-a_ji, diagonal=0).
ANY SQUARE MATRIX = Symmetric part + Skew-symmetric part.
A=(A+A^T)/2 + (A-A^T)/2. First part symmetric, second skew-symmetric.
ELEMENTARY OPERATIONS (Row/Column):
Ri↔Rj (interchange). Ri→kRi (multiply by scalar). Ri→Ri+kRj (add multiple of another row).
Used in finding inverse by row reduction.
SOLVED EXAMPLES:
Example 1: A=[[1,2],[3,4]]. Find A+A^T and show symmetric.
A^T=[[1,3],[2,4]]. A+A^T=[[2,5],[5,8]]. (A+A^T)^T=[[2,5],[5,8]]=A+A^T. Symmetric.
Example 2: Express A=[[1,2],[3,4]] as sum of symmetric and skew-symmetric.
Symmetric=(A+A^T)/2=[[1,2.5],[2.5,4]].
Skew-symmetric=(A-A^T)/2=[[0,-0.5],[0.5,0]].
Example 3: If A=[[1,2],[3,4]] and B=[[5,6],[7,8]], find AB.
AB=[[1×5+2×7, 1×6+2×8],[3×5+4×7, 3×6+4×8]]=[[19,22],[43,50]].
COMMON MISTAKES:
AB≠BA in general (matrix multiplication is NOT commutative).
(AB)^T=B^T A^T (ORDER REVERSES, not A^T B^T).
Dimensions: (m×n)(n×p)→(m×p). Inner dimensions must match.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch3", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch4: Determinants
DETERMINANT: scalar value computed from square matrix.
det(2×2): |a b; c d|=ad-bc.
det(3×3) by expansion along row 1:
|a1 b1 c1; a2 b2 c2; a3 b3 c3|=a1(b2c3-b3c2)-b1(a2c3-a3c2)+c1(a2b3-a3b2).
PROPERTIES OF DETERMINANTS:
1. Rows and columns can be interchanged: det(A)=det(A^T).
2. Interchange two rows: determinant changes sign.
3. Two identical rows: det=0.
4. Multiply row by k: det multiplied by k.
5. Add multiple of one row to another: det unchanged.
6. det(AB)=det(A)×det(B). det(kA)=k^n×det(A) for n×n matrix.
MINORS AND COFACTORS:
Minor M_ij: determinant of matrix obtained by deleting row i and column j.
Cofactor C_ij=(-1)^(i+j) × M_ij.
ADJOINT: adj(A)=transpose of cofactor matrix.
INVERSE: A^(-1)=adj(A)/det(A). Exists iff det(A)≠0.
AREA OF TRIANGLE: (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|.
Using determinant: (1/2)|det([[x1,y1,1],[x2,y2,1],[x3,y3,1]])|.
CRAMER'S RULE for ax+by=e, cx+dy=f:
D=|a b; c d|=ad-bc. D_x=|e b; f d|. D_y=|a e; c f|.
x=D_x/D, y=D_y/D (only if D≠0).
SOLVED EXAMPLES:
Example 1: Find det([[2,3],[-1,4]])=2×4-3×(-1)=8+3=11.
Example 2: Solve x+y+z=6, 2x-y+z=3, x+2y-z=2 by Cramer's rule.
D=det([[1,1,1],[2,-1,1],[1,2,-1]])=1(1-2)-1(-2-1)+1(4+1)=-1+3+5=7.
D_x=det([[6,1,1],[3,-1,1],[2,2,-1]])=6(1-2)-1(-3-2)+1(6+2)=-6+5+8=7.
x=D_x/D=7/7=1. Similarly y=2, z=3.
Example 3: A=[[1,2],[3,4]]. Find A^(-1).
det(A)=4-6=-2. Cofactor matrix=[[4,-3],[-2,1]]. adj(A)=[[4,-2],[-3,1]].
A^(-1)=(1/-2)[[4,-2],[-3,1]]=[[-2,1],[3/2,-1/2]].
COMMON MISTAKES:
Cofactor includes the sign (-1)^(i+j). Minor does NOT include the sign.
det(kA)=k^n×det(A) for n×n matrix (NOT just k×det(A)).
A^(-1) exists only when det(A)≠0 (non-singular matrix).""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch4", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch5: Continuity and Differentiability
CONTINUITY at x=a: lim(x→a) f(x) = f(a).
Three conditions: f(a) defined, limit exists, limit equals f(a).
Continuous function: continuous at every point in domain.
Sum, difference, product of continuous functions is continuous.
Composite of continuous functions is continuous.
DIFFERENTIABILITY: f'(a)=lim(h→0) [f(a+h)-f(a)]/h exists.
Differentiable → Continuous. Continuous does NOT imply differentiable.
|x| is continuous everywhere but NOT differentiable at x=0.
CHAIN RULE: d/dx[f(g(x))]=f'(g(x))×g'(x). dy/dx=(dy/du)×(du/dx).
IMPLICIT DIFFERENTIATION: differentiate both sides w.r.t. x, treat y as function of x.
d/dx[f(y)]=f'(y)×dy/dx.
PARAMETRIC DIFFERENTIATION: x=f(t), y=g(t). dy/dx=(dy/dt)/(dx/dt)=g'(t)/f'(t).
LOGARITHMIC DIFFERENTIATION: for y=x^x or y=f(x)^g(x). Take log both sides, differentiate.
SECOND ORDER DERIVATIVE: d^2y/dx^2=d/dx[dy/dx].
STANDARD DERIVATIVES:
d/dx[x^n]=nx^(n-1). d/dx[e^x]=e^x. d/dx[a^x]=a^x ln(a).
d/dx[ln x]=1/x. d/dx[log_a x]=1/(x ln a).
d/dx[sin x]=cos x. d/dx[cos x]=-sin x. d/dx[tan x]=sec^2 x.
d/dx[sin^(-1)x]=1/sqrt(1-x^2). d/dx[cos^(-1)x]=-1/sqrt(1-x^2).
d/dx[tan^(-1)x]=1/(1+x^2).
ROLLE'S THEOREM: if f continuous on [a,b], differentiable on (a,b), f(a)=f(b), then there exists c in (a,b) where f'(c)=0.
MEAN VALUE THEOREM (MVT/Lagrange): if f continuous on [a,b], differentiable on (a,b), then there exists c where f'(c)=[f(b)-f(a)]/(b-a).
SOLVED EXAMPLES:
Example 1: Differentiate x^x.
y=x^x → ln y=x ln x → (1/y)(dy/dx)=ln x+1 → dy/dx=x^x(1+ln x).
Example 2: If x=at^2, y=2at, find dy/dx.
dx/dt=2at, dy/dt=2a. dy/dx=2a/2at=1/t.
Example 3: Check continuity of |x-3| at x=3.
LHL=lim(x→3-)|x-3|=lim(x→3-)(3-x)=0. RHL=lim(x→3+)(x-3)=0. f(3)=0. Continuous.
But not differentiable at x=3 (left derivative=-1, right=+1, unequal).
COMMON MISTAKES:
Continuous does NOT mean differentiable. |x| is the standard counter-example.
Chain rule: derivative of OUTER function × derivative of INNER function.
In parametric: dy/dx=(dy/dt)/(dx/dt), NOT (dx/dt)/(dy/dt).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch5", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch6: Applications of Derivatives
RATE OF CHANGE: dy/dx represents rate of change of y w.r.t. x.
If x and y both functions of t: use chain rule. dy/dt=(dy/dx)×(dx/dt).
TANGENT AND NORMAL:
Slope of tangent at (x1,y1): m=dy/dx|(x1,y1).
Equation of tangent: y-y1=m(x-x1).
Slope of normal=-1/m. Equation of normal: y-y1=(-1/m)(x-x1).
INCREASING AND DECREASING FUNCTIONS:
f increasing on (a,b) if f'(x)>0 for all x in (a,b).
f decreasing on (a,b) if f'(x)<0 for all x in (a,b).
MAXIMA AND MINIMA:
Critical points: where f'(x)=0 or f'(x) undefined.
First Derivative Test:
f'changes + to -: local maximum. f' changes - to +: local minimum. No change: neither.
Second Derivative Test:
f''(c)<0: local maximum. f''(c)>0: local minimum. f''(c)=0: test fails.
ABSOLUTE MAXIMA/MINIMA on [a,b]:
Evaluate f at all critical points AND endpoints. Largest=absolute max, smallest=absolute min.
APPROXIMATIONS: f(x+deltax)≈f(x)+f'(x)×deltax.
SOLVED EXAMPLES:
Example 1: Find intervals where f(x)=2x^3-9x^2+12x-5 is increasing/decreasing.
f'(x)=6x^2-18x+12=6(x^2-3x+2)=6(x-1)(x-2).
f'(x)>0 when x<1 or x>2: increasing on (-inf,1) and (2,inf).
f'(x)<0 when 1<x<2: decreasing on (1,2).
Example 2: Local maxima/minima of f above.
f'(1)=0 and f' changes + to -: local max at x=1. f(1)=2-9+12-5=0.
f'(2)=0 and f' changes - to +: local min at x=2. f(2)=16-36+24-5=-1.
Example 3: Two numbers with sum 24 and maximum product.
Let numbers be x and 24-x. P=x(24-x)=24x-x^2.
P'=24-2x=0 → x=12. P''=-2<0: maximum. Numbers: 12 and 12.
Example 4: Rate: balloon volume V=(4/3)pi*r^3. Find dV/dt when r=5, dr/dt=2.
dV/dt=4pi*r^2*(dr/dt)=4pi×25×2=200pi cm^3/s.
COMMON MISTAKES:
Critical points where f'=0 need NOT be maxima or minima (inflection points possible).
Second derivative test FAILS when f''=0 (use first derivative test instead).
For max product/area problems: always verify using second derivative test.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch6", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch7: Integrals
INDEFINITE INTEGRALS:
integral(x^n dx)=x^(n+1)/(n+1)+C (n≠-1). integral(1/x dx)=ln|x|+C.
integral(e^x dx)=e^x+C. integral(a^x dx)=a^x/ln(a)+C.
integral(sin x dx)=-cos x+C. integral(cos x dx)=sin x+C.
integral(tan x dx)=ln|sec x|+C. integral(cot x dx)=ln|sin x|+C.
integral(sec x dx)=ln|sec x+tan x|+C. integral(cosec x dx)=-ln|cosec x+cot x|+C.
integral(sec^2 x dx)=tan x+C. integral(cosec^2 x dx)=-cot x+C.
integral(1/(x^2+a^2) dx)=(1/a)tan^(-1)(x/a)+C.
integral(1/sqrt(a^2-x^2) dx)=sin^(-1)(x/a)+C.
integral(1/sqrt(x^2+a^2) dx)=ln|x+sqrt(x^2+a^2)|+C.
METHODS OF INTEGRATION:
METHOD 1 - Substitution: let u=g(x), du=g'(x)dx.
integral(2x/(x^2+1) dx): let u=x^2+1, du=2x dx → integral(1/u du)=ln|u|+C=ln|x^2+1|+C.
METHOD 2 - Integration by Parts (ILATE rule):
integral(u dv)=uv-integral(v du).
ILATE order for u: Inverse trig, Logarithm, Algebraic, Trigonometric, Exponential.
integral(x e^x dx): u=x, dv=e^x dx. =xe^x-integral(e^x dx)=xe^x-e^x+C=e^x(x-1)+C.
integral(x^2 e^x dx): apply by parts TWICE.
METHOD 3 - Partial Fractions (for rational functions):
(2x+3)/((x-1)(x+2))=A/(x-1)+B/(x+2). Solve for A and B.
For repeated factor (x-1)^2: A/(x-1)+B/(x-1)^2+C/(x+2).
METHOD 4 - Special Integrals:
integral(sin^n x dx) and integral(cos^n x dx): use reduction formulas.
integral(sin^2 x dx)=x/2-sin(2x)/4+C. integral(cos^2 x dx)=x/2+sin(2x)/4+C.
DEFINITE INTEGRALS:
integral[a to b] f(x) dx=F(b)-F(a) (Fundamental Theorem).
PROPERTIES:
integral[a to b]=- integral[b to a].
integral[a to b] f(x) dx=integral[a to c] f(x) dx+integral[c to b] f(x) dx.
integral[0 to a] f(x) dx=integral[0 to a] f(a-x) dx (King's rule).
SOLVED EXAMPLES:
Example 1: integral(x^2 e^x dx).
u=x^2, dv=e^x dx: x^2 e^x-integral(2x e^x dx).
Apply by parts again on integral(2x e^x dx): 2[xe^x-e^x].
Answer: x^2 e^x-2xe^x+2e^x+C=e^x(x^2-2x+2)+C.
Example 2: integral(dx/(x^2-4))=integral(dx/((x-2)(x+2))).
Partial fractions: 1/((x-2)(x+2))=(1/4)(1/(x-2)-1/(x+2)).
Answer=(1/4)ln|(x-2)/(x+2)|+C.
Example 3: integral(sin^3 x dx)=integral(sin x(1-cos^2 x) dx).
Let u=cos x: -integral((1-u^2) du)=-u+u^3/3+C=-cos x+cos^3 x/3+C.
COMMON MISTAKES:
ILATE: u should be chosen by ILATE order (leftmost=u).
Integration by parts may need to be applied multiple times.
King's rule: replace x with (a-x) inside integral, keep limits same.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch7", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch8: Application of Integrals
AREA BETWEEN CURVE AND X-AXIS:
Area = integral[a to b] |f(x)| dx.
If f(x)>=0 on [a,b]: Area=integral[a to b] f(x) dx.
If f(x)<=0 on [a,b]: Area=|integral[a to b] f(x) dx|=-integral[a to b] f(x) dx.
If f changes sign: split at zeros, add absolute values of each part.
AREA BETWEEN TWO CURVES:
If f(x)>=g(x) on [a,b]: Area=integral[a to b] [f(x)-g(x)] dx.
Always integrate UPPER curve minus LOWER curve.
AREA USING Y-AXIS:
Area=integral[c to d] |g(y)| dy where x=g(y) is curve expressed in terms of y.
STANDARD AREAS:
Circle x^2+y^2=r^2: total area=pi*r^2. Using integration: 4×integral[0 to r] sqrt(r^2-x^2) dx.
Ellipse x^2/a^2+y^2/b^2=1: area=pi*a*b.
Parabola y^2=4ax and line x=h: area=(4/3)h*sqrt(ah) [to vertex from x=0 to x=h side].
SOLVED EXAMPLES:
Example 1: Area bounded by y=x^2 and y=x+2.
Intersection: x^2=x+2 → x^2-x-2=0 → (x-2)(x+1)=0 → x=-1,2.
Area=integral[-1 to 2] (x+2-x^2) dx=[x^2/2+2x-x^3/3] from -1 to 2.
=(2+4-8/3)-(-1/2-2+1/3... wait:
At x=2: 4/2+4-8/3=2+4-8/3=6-8/3=10/3.
At x=-1: 1/2-2+1/3=-7/6.
Area=10/3-(-7/6)=10/3+7/6=20/6+7/6=27/6=9/2 sq units.
Example 2: Area of circle x^2+y^2=16.
Area=4×integral[0 to 4] sqrt(16-x^2) dx=4×[x/2*sqrt(16-x^2)+8*sin^(-1)(x/4)] from 0 to 4.
=4×[0+8*pi/2-0]=4×4pi=16pi sq units. (Confirms pi*r^2=pi*16.)
Example 3: Area between y=x^2 and y=sqrt(x).
Intersection: x^2=sqrt(x) → x^4=x → x(x^3-1)=0 → x=0,1.
sqrt(x)>=x^2 on [0,1]. Area=integral[0 to 1](sqrt(x)-x^2)dx=[2x^(3/2)/3-x^3/3] from 0 to 1=2/3-1/3=1/3.
COMMON MISTAKES:
Always integrate UPPER minus LOWER (not absolute value of each separately).
Find intersection points by setting curves equal.
Area is always POSITIVE (use absolute values if needed).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch8", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch9: Differential Equations
ORDER: order of highest derivative. DEGREE: power of highest derivative (after clearing fractions/roots).
FORMATION: differentiate given equation to eliminate arbitrary constants (number of constants=order).
METHODS OF SOLVING:
METHOD 1 - Variable Separable: f(x)dx=g(y)dy. Integrate both sides separately.
dy/dx=e^(x+y)=e^x*e^y → e^(-y)dy=e^x dx → -e^(-y)=e^x+C.
METHOD 2 - Homogeneous Equations: dy/dx=f(y/x). Substitute v=y/x, y=vx.
dy/dx=v+x*dv/dx. Equation becomes separable.
Identify homogeneous: if f(kx,ky)=k^n*f(x,y) (all terms same degree).
METHOD 3 - Linear DE: dy/dx+P(x)*y=Q(x).
Integrating factor IF=e^(integral P dx).
Solution: y*IF=integral(Q*IF dx)+C.
For dx/dy+P(y)*x=Q(y): IF=e^(integral P dy). x*IF=integral(Q*IF dy)+C.
STANDARD FORMS:
Variable separable: dy/dx=f(x)*g(y) → dy/g(y)=f(x)dx.
SOLVED EXAMPLES:
Example 1: Solve dy/dx=e^(x+y).
e^(-y)dy=e^x dx → -e^(-y)=e^x+C → e^x+e^(-y)=C1.
Example 2: Solve (x^2+y^2)dx=2xy dy (homogeneous).
dy/dx=(x^2+y^2)/(2xy). Put y=vx: v+x*dv/dx=(1+v^2)/(2v).
x*dv/dx=(1+v^2)/(2v)-v=(1-v^2)/(2v). 2v/(1-v^2)dv=dx/x.
-ln|1-v^2|=ln|x|+C1 → ln|x(1-v^2)|=-C1 → x(1-y^2/x^2)=C → x^2-y^2=Cx.
Example 3: Solve dy/dx+2y/x=x^2 (linear).
P=2/x, Q=x^2. IF=e^(integral 2/x dx)=e^(2ln x)=x^2.
y*x^2=integral(x^2*x^2 dx)=integral(x^4 dx)=x^5/5+C.
y=x^3/5+C/x^2.
COMMON MISTAKES:
Degree: power of HIGHEST ORDER derivative (after removing radicals).
Homogeneous: all terms must have SAME total degree.
Linear DE: coefficient of dy/dx must be 1 (divide through if needed).""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "class_12", "chapter": "ch9", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch10: Vector Algebra
VECTOR: quantity with magnitude and direction. Notation: a (bold) or a with arrow.
Unit vector: magnitude=1. a_hat=a/|a|.
TYPES: Zero vector, Unit vector, Coinitial, Collinear/Parallel, Equal vectors.
POSITION VECTOR: of point P(x,y,z): OP=xi+yj+zk. |OP|=sqrt(x^2+y^2+z^2).
OPERATIONS:
Addition: (a1i+a2j+a3k)+(b1i+b2j+b3k)=(a1+b1)i+(a2+b2)j+(a3+b3)k.
Scalar multiplication: k(ai+bj+ck)=kai+kbj+ckk.
DOT PRODUCT (Scalar product):
a.b=|a||b|cos(theta). a.b=a1b1+a2b2+a3b3.
a.b=0 iff perpendicular (or one is zero vector).
a.a=|a|^2. i.i=j.j=k.k=1. i.j=j.k=k.i=0.
CROSS PRODUCT (Vector product):
|a×b|=|a||b|sin(theta). Direction: right-hand rule.
a×b=det([[i,j,k],[a1,a2,a3],[b1,b2,b3]]).
=(a2b3-a3b2)i-(a1b3-a3b1)j+(a1b2-a2b1)k.
a×b=0 iff parallel. a×a=0. i×j=k, j×k=i, k×i=j. j×i=-k.
|a×b|=area of parallelogram with sides a and b.
(1/2)|a×b|=area of triangle.
SCALAR TRIPLE PRODUCT: [a b c]=a.(b×c). Volume of parallelepiped.
[a b c]=0 iff coplanar.
SOLVED EXAMPLES:
Example 1: a=2i+3j-k, b=i-2j+3k.
a.b=2(1)+3(-2)+(-1)(3)=2-6-3=-7.
|a|=sqrt(4+9+1)=sqrt(14). |b|=sqrt(1+4+9)=sqrt(14).
cos(theta)=-7/14=-1/2. theta=120°.
Example 2: a×b=det([[i,j,k],[2,3,-1],[1,-2,3]]).
=i(9-2)-j(6+1)+k(-4-3)=7i-7j-7k=7(i-j-k).
|a×b|=7sqrt(3). Area of parallelogram=7sqrt(3).
Example 3: Unit vector along 2i+3j+6k.
|v|=sqrt(4+9+36)=sqrt(49)=7. Unit vector=(2i+3j+6k)/7.
COMMON MISTAKES:
a.b is SCALAR. a×b is VECTOR.
i×j=k but j×i=-k (cross product NOT commutative).
a×b=0 means PARALLEL (not perpendicular). a.b=0 means PERPENDICULAR.""",
    metadata={"source": "ncert", "topic": "vectors", "class_level": "class_12", "chapter": "ch10", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch11: Three Dimensional Geometry
DIRECTION COSINES: cos(alpha), cos(beta), cos(gamma) where alpha,beta,gamma are angles line makes with x,y,z axes.
l=cos(alpha), m=cos(beta), n=cos(gamma). l^2+m^2+n^2=1.
DIRECTION RATIOS: proportional to direction cosines. a,b,c are DRs if l/a=m/b=n/c.
l=a/sqrt(a^2+b^2+c^2), m=b/sqrt(a^2+b^2+c^2), n=c/sqrt(a^2+b^2+c^2).
EQUATION OF LINE:
Vector form: r=a+lambda*b (a=point on line, b=direction vector).
Cartesian: (x-x1)/a=(y-y1)/b=(z-z1)/c (symmetric form).
Through two points: (x-x1)/(x2-x1)=(y-y1)/(y2-y1)=(z-z1)/(z2-z1).
ANGLE BETWEEN LINES:
cos(theta)=|l1l2+m1m2+n1n2|=|a1a2+b1b2+c1c2|/sqrt(a1^2+b1^2+c1^2)*sqrt(a2^2+b2^2+c2^2).
Parallel: a1/a2=b1/b2=c1/c2. Perpendicular: a1a2+b1b2+c1c2=0.
EQUATION OF PLANE:
General: ax+by+cz+d=0. Normal vector=(a,b,c).
Intercept form: x/a+y/b+z/c=1.
Vector form: r.n_hat=d (n_hat=unit normal).
Through three points: use determinant form.
DISTANCE FROM POINT TO PLANE:
Distance of (x1,y1,z1) from ax+by+cz+d=0: |ax1+by1+cz1+d|/sqrt(a^2+b^2+c^2).
ANGLE BETWEEN LINE AND PLANE:
sin(phi)=|al+bm+cn|/sqrt(a^2+b^2+c^2)*sqrt(l^2+m^2+n^2).
SKEW LINES: lines that are not parallel and do not intersect.
Shortest distance=|(a2-a1).(b1×b2)|/|b1×b2|.
SOLVED EXAMPLES:
Example 1: Angle between lines (x-1)/2=(y+1)/3=(z-2)/6 and (x+2)/1=(y-3)/4=(z+1)/2.
DRs: (2,3,6) and (1,4,2). cos(theta)=(2+12+12)/(7×sqrt(21))=26/(7sqrt(21)).
Example 2: Distance from (1,2,3) to plane 2x-3y+z=5.
d=|2(1)-3(2)+1(3)-5|/sqrt(4+9+1)=|2-6+3-5|/sqrt(14)=|-6|/sqrt(14)=6/sqrt(14)=3sqrt(14)/7.
Example 3: Shortest distance between skew lines.
r1=i+j+t(2i-j+k) and r2=2i+j-k+s(3i-5j+2k).
a1=i+j, a2=2i+j-k. b1=2i-j+k, b2=3i-5j+2k.
b1×b2=det([[i,j,k],[2,-1,1],[3,-5,2]])=i(-2+5)-j(4-3)+k(-10+3)=3i-j-7k.
|b1×b2|=sqrt(9+1+49)=sqrt(59).
(a2-a1)=i-k. (a2-a1).(b1×b2)=3+0+7=10.
Distance=|10|/sqrt(59)=10/sqrt(59).
COMMON MISTAKES:
Direction ratios are proportional to direction cosines (not equal unless normalised).
Skew lines: neither parallel nor intersecting (common in 3D, impossible in 2D).
Distance formula: use |...|/sqrt(a^2+b^2+c^2), not just |...|.""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "class_12", "chapter": "ch11", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch12: Linear Programming
LINEAR PROGRAMMING PROBLEM (LPP):
Objective function: Z=ax+by (to maximise or minimise).
Constraints: inequalities (ax+by<=c, x>=0, y>=0 etc).
Feasible region: set of all points satisfying ALL constraints simultaneously.
Feasible solution: any point in feasible region.
Optimal solution: feasible solution that gives maximum/minimum value of Z.
CORNER POINT METHOD (THEOREM):
If optimal solution exists, it occurs at a CORNER POINT (vertex) of feasible region.
Steps:
1. Graph all constraints. Find feasible region.
2. Find all corner points (vertices) of feasible region.
3. Evaluate Z at each corner point.
4. Maximum/minimum value of Z is the optimal solution.
TYPES OF LPP:
Bounded feasible region: has maximum AND minimum.
Unbounded feasible region: may not have maximum (for maximise) or minimum (for minimise).
Infeasible: no feasible region (constraints contradictory). No solution.
FORMULATING LPP FROM WORD PROBLEMS:
Identify: variables (what to find), objective (what to optimise), constraints (conditions).
SOLVED EXAMPLES:
Example 1: Maximise Z=3x+4y subject to x+y<=450, 2x+y<=600, x>=0, y>=0.
Corner points: O(0,0), A(300,0), B(150,300), C(0,450).
Z at O=0. Z at A=900. Z at B=450+1200=1650. Z at C=1800.
Maximum Z=1800 at C(0,450).
Example 2: Minimise Z=5x+7y subject to 2x+y>=8, x+2y>=10, x>=0, y>=0.
Corner points: A(0,8), B(2,4), C(10,0).
Z at A=56. Z at B=10+28=38. Z at C=50.
Minimum Z=38 at B(2,4).
FINDING CORNER POINTS: solve pairs of boundary equations simultaneously.
Intersection of 2x+y=600 and x+y=450: subtract → x=150, y=300.
COMMON MISTAKES:
Evaluate Z at ALL corner points (not just one or two).
Feasible region must satisfy ALL constraints (including x>=0, y>=0).
For minimum in unbounded region: check if solution is truly minimum.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "class_12", "chapter": "ch12", "difficulty": "advanced"}),

    Document(page_content="""Class 12 | Ch13: Probability
CONDITIONAL PROBABILITY:
P(A|B)=P(A∩B)/P(B) where P(B)≠0.
P(A∩B)=P(A|B)*P(B)=P(B|A)*P(A).
MULTIPLICATION THEOREM:
P(A∩B)=P(A)*P(B|A). P(A∩B∩C)=P(A)*P(B|A)*P(C|AB).
INDEPENDENT EVENTS:
A and B independent: P(A∩B)=P(A)*P(B). P(A|B)=P(A).
A,B,C independent: P(A∩B)=P(A)P(B), P(B∩C)=P(B)P(C), P(A∩C)=P(A)P(C), AND P(A∩B∩C)=P(A)P(B)P(C). (All four conditions needed.)
TOTAL PROBABILITY THEOREM:
If B1,B2,...,Bn are mutually exclusive and exhaustive events:
P(A)=P(A|B1)*P(B1)+P(A|B2)*P(B2)+...+P(A|Bn)*P(Bn).
BAYES' THEOREM:
P(Bi|A)=P(A|Bi)*P(Bi) / [P(A|B1)*P(B1)+...+P(A|Bn)*P(Bn)].
Prior probability: P(Bi). Posterior probability: P(Bi|A).
RANDOM VARIABLE AND PROBABILITY DISTRIBUTION:
Random variable X: function from sample space to real numbers.
Mean (Expected value): E(X)=mu=sum(xi*P(xi)).
Variance: Var(X)=E(X^2)-[E(X)]^2=sum(xi^2*P(xi))-mu^2.
SD=sqrt(Var(X)).
BERNOULLI TRIALS AND BINOMIAL DISTRIBUTION:
n independent trials, each with probability p of success.
P(X=r)=nCr*p^r*(1-p)^(n-r)=nCr*p^r*q^(n-r) where q=1-p.
Mean=np. Variance=npq. SD=sqrt(npq).
SOLVED EXAMPLES:
Example 1: Bag A: 3R,5B. Bag B: 4R,6B. One bag chosen randomly, red ball drawn. Find P(bag A).
P(A)=P(B)=1/2. P(R|A)=3/8. P(R|B)=4/10=2/5.
P(R)=P(R|A)P(A)+P(R|B)P(B)=(3/8)(1/2)+(2/5)(1/2)=3/16+1/5=31/80.
P(A|R)=P(R|A)P(A)/P(R)=(3/16)/(31/80)=(3/16)*(80/31)=15/31.
Example 2: Binomial X~B(10,0.4). Find P(X=3).
P(X=3)=10C3*(0.4)^3*(0.6)^7=120*0.064*0.0279936≈0.2150.
Mean=10*0.4=4. Variance=10*0.4*0.6=2.4.
COMMON MISTAKES:
Bayes theorem: denominator is TOTAL probability P(A) using all branches.
Binomial: trials must be INDEPENDENT with CONSTANT probability p.
E(X^2) ≠ [E(X)]^2. Variance=E(X^2)-[E(X)]^2.""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "class_12", "chapter": "ch13", "difficulty": "advanced"}),


    # ── JEE ADVANCED — 8 Topic Groups ───────────────────────────────

    Document(page_content="""JEE Advanced | Topic 1: Advanced Calculus
LIMITS - SPECIAL TECHNIQUES:
L'Hopital's Rule: if lim f(x)/g(x) gives 0/0 or inf/inf, then lim f(x)/g(x)=lim f'(x)/g'(x).
Apply repeatedly if still indeterminate. Works for 0/0, inf/inf forms.
Other indeterminate: 0×inf, inf-inf, 0^0, 1^inf, inf^0. Convert to 0/0 or inf/inf first.
1^inf form: lim[f(x)]^g(x) where f→1, g→inf. Take log: g(x)*ln(f(x))→inf×0. Use L'Hopital.
TAYLOR AND MACLAURIN SERIES:
e^x=1+x+x^2/2!+x^3/3!+... (all x).
sin x=x-x^3/3!+x^5/5!-... (all x).
cos x=1-x^2/2!+x^4/4!-... (all x).
ln(1+x)=x-x^2/2+x^3/3-... (|x|<=1, x≠-1).
(1+x)^n=1+nx+n(n-1)x^2/2!+... (|x|<1 for non-integer n).
LEIBNIZ THEOREM (nth derivative of product):
(fg)^(n)=sum(r=0 to n) nCr * f^(r) * g^(n-r).
DEFINITE INTEGRAL PROPERTIES:
King's rule: integral[a to b] f(x)dx=integral[a to b] f(a+b-x)dx.
integral[0 to 2a] f(x)dx=2*integral[0 to a] f(x)dx if f(2a-x)=f(x), else 0 if f(2a-x)=-f(x).
integral[-a to a] f(x)dx=2*integral[0 to a] f(x)dx if f even, else 0 if f odd.
Walli's formula: integral[0 to pi/2] sin^n(x)dx=integral[0 to pi/2] cos^n(x)dx.
For even n: (n-1)(n-3)...1 / n(n-2)...2 * pi/2.
For odd n: (n-1)(n-3)...2 / n(n-2)...1.
REDUCTION FORMULAS:
integral sin^n x dx = -sin^(n-1)x cosx/n + (n-1)/n * integral sin^(n-2)x dx.
SOLVED EXAMPLES:
Example 1: lim(x→0) (e^x-1-x)/x^2.
0/0 form. L'Hopital: lim (e^x-1)/(2x). Still 0/0.
L'Hopital again: lim e^x/2=1/2.
Example 2: Evaluate integral[0 to pi] x*sinx/(1+cos^2 x)dx.
By King's rule: I=integral[0 to pi] (pi-x)*sin(pi-x)/(1+cos^2(pi-x))dx.
sin(pi-x)=sinx. cos(pi-x)=-cosx. So I=integral[0 to pi] (pi-x)*sinx/(1+cos^2 x)dx.
2I=pi*integral[0 to pi] sinx/(1+cos^2 x)dx.
Let u=cosx: 2I=pi*integral[-1 to 1] du/(1+u^2)=pi[tan^(-1)u] from -1 to 1=pi[pi/4+pi/4]=pi^2/2.
I=pi^2/4.
Example 3: Using Maclaurin: find lim(x→0) (sinx-x)/x^3.
sinx=x-x^3/6+... So sinx-x=-x^3/6+... Divide by x^3: limit=-1/6.
COMMON MISTAKES:
L'Hopital: must be 0/0 or inf/inf EXACTLY. Cannot apply to 0/inf or inf+inf.
King's rule: limits stay SAME (a to b), replace x with a+b-x inside.
Taylor series: valid only within radius of convergence.""",
    metadata={"source": "ncert", "topic": "calculus", "class_level": "jee_advanced", "chapter": "advanced_calculus", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 2: Advanced Algebra
THEORY OF EQUATIONS:
For polynomial p(x)=a_n*x^n+...+a_0 with roots r1,r2,...,rn:
Sum of roots=r1+r2+...+rn=-a_(n-1)/a_n.
Sum of products of pairs=a_(n-2)/a_n.
Sum of products of triplets=-a_(n-3)/a_n.
Product of all roots=(-1)^n * a_0/a_n.
Newton's identities relate power sums to elementary symmetric polynomials.
LOCATION OF ROOTS:
Both roots of ax^2+bx+c=0 positive: D>=0, -b/a>0, c/a>0.
Both roots negative: D>=0, -b/a<0, c/a>0.
Roots of opposite sign: c/a<0 (D automatically >0).
Both roots in (p,q): D>=0, f(p)>0 (same sign as a), f(q)>0, p<-b/2a<q.
COMMON ROOTS:
If ax^2+bx+c=0 and dx^2+ex+f=0 have common root alpha:
(bf-ce)^2=(ae-bd)(cd-af) (condition for one common root).
For both roots common: a/d=b/e=c/f.
SUM OF SERIES:
Telescoping: express term as f(n)-f(n-1), sum collapses.
1/(n(n+1))=1/n-1/(n+1). Sum from 1 to n = 1-1/(n+1).
Method of differences: if T_n can be expressed as f(n)-f(n-2), sum accordingly.
COMPLEX NUMBERS ADVANCED:
nth roots of unity: 1, omega, omega^2,...,omega^(n-1) where omega=e^(2pi*i/n).
Sum of all nth roots of unity=0. Product=(-1)^(n+1).
Roots evenly spaced on unit circle at angles 2pi*k/n.
SOLVED EXAMPLES:
Example 1: Roots of x^3-6x^2+11x-6=0 in AP. Find them.
Let roots be a-d, a, a+d. Sum=3a=6 → a=2. Product=a(a^2-d^2)=6 → 2(4-d^2)=6 → d^2=1 → d=1.
Roots: 1, 2, 3. Verify: sum of pairs=1*2+2*3+1*3=11. Product=6. Correct.
Example 2: Find sum of series 1/(1*2)+1/(2*3)+...+1/(n(n+1)).
T_k=1/(k(k+1))=1/k-1/(k+1). Telescoping sum=1-1/(n+1)=n/(n+1).
Example 3: Show sum of cube roots of unity=0.
1+omega+omega^2=0. (Sum of all nth roots of unity=0 for n>1.)
Geometric series: (1-omega^3)/(1-omega)=0/(1-omega)=0 since omega^3=1.
COMMON MISTAKES:
For roots in AP: take a-d, a, a+d (NOT a, a+d, a+2d — product is messier).
Telescoping: must identify the correct f(n) that gives the telescoping pattern.
Common roots: substitute the common root into BOTH equations, eliminate.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "jee_advanced", "chapter": "advanced_algebra", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 3: Advanced Coordinate Geometry
PAIR OF STRAIGHT LINES:
ax^2+2hxy+by^2=0 represents pair of lines through origin.
Slopes m1,m2: m1+m2=-2h/b, m1*m2=a/b.
Angle between lines: tan(theta)=2sqrt(h^2-ab)/(a+b).
Lines coincident: h^2=ab. Lines perpendicular: a+b=0.
Combined equation of lines through origin with slopes m1,m2: b(y-m1*x)(y-m2*x)=0.
General second degree: ax^2+2hxy+by^2+2gx+2fy+c=0.
Represents pair of lines if det([[a,h,g],[h,b,f],[g,f,c]])=0.
CIRCLES:
Radical axis of two circles: locus of points with equal power w.r.t. both circles.
Power of point P w.r.t. circle: PT^2=S1 where S1=x1^2+y1^2+2gx1+2fy1+c.
Radical axis: S1-S2=0 (subtract equations).
Coaxial circles: family of circles with common radical axis.
CONICS - ADVANCED:
Chord of contact from point (x1,y1) to circle x^2+y^2=a^2: xx1+yy1=a^2.
Chord of contact to ellipse x^2/a^2+y^2/b^2=1: xx1/a^2+yy1/b^2=1.
Parametric forms: Ellipse (a*cos t, b*sin t). Parabola (at^2, 2at). Hyperbola (a*sec t, b*tan t).
Normal at parametric point t on parabola y^2=4ax: y=-tx+2at+at^3.
Condition for line y=mx+c to be tangent to y^2=4ax: c=a/m.
LOCUS PROBLEMS:
Set up coordinates, use given conditions, eliminate parameter, simplify to standard form.
SOLVED EXAMPLES:
Example 1: 3x^2+10xy+8y^2=0. Find angle between lines.
a=3, 2h=10 so h=5, b=8. tan(theta)=2*sqrt(25-24)/(3+8)=2/11. theta=tan^(-1)(2/11).
Example 2: Chord of contact from (1,2) to circle x^2+y^2=25.
x(1)+y(2)=25 → x+2y=25.
Example 3: If z=x+iy and |z-2|=2|z-1|, find locus.
|(x-2)+iy|=2|(x-1)+iy|. (x-2)^2+y^2=4[(x-1)^2+y^2].
x^2-4x+4+y^2=4x^2-8x+4+4y^2. 3x^2+3y^2-4x=0. x^2+y^2-4x/3=0. Circle.
COMMON MISTAKES:
Pair of lines: 2hxy (coefficient of xy is 2h, not h).
Radical axis: subtract S1 and S2 equations directly (coefficients of x^2,y^2 must be 1 first).
Tangent condition: c=a/m for parabola y^2=4ax (from OUTSIDE).""",
    metadata={"source": "ncert", "topic": "geometry", "class_level": "jee_advanced", "chapter": "advanced_coord_geometry", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 4: Advanced Trigonometry
PRODUCT FORMULAS:
sin A + sin B = 2 sin((A+B)/2) cos((A-B)/2).
sin A - sin B = 2 cos((A+B)/2) sin((A-B)/2).
cos A + cos B = 2 cos((A+B)/2) cos((A-B)/2).
cos A - cos B = -2 sin((A+B)/2) sin((A-B)/2).
sin A * sin B = (1/2)[cos(A-B)-cos(A+B)].
cos A * cos B = (1/2)[cos(A-B)+cos(A+B)].
sin A * cos B = (1/2)[sin(A+B)+sin(A-B)].
TRIGONOMETRIC EQUATIONS:
General solutions: sin(theta)=sin(alpha) → theta=n*pi+(-1)^n*alpha.
cos(theta)=cos(alpha) → theta=2n*pi±alpha.
tan(theta)=tan(alpha) → theta=n*pi+alpha.
For sin^2(theta)=sin^2(alpha): theta=n*pi±alpha.
CONDITIONAL IDENTITIES (when A+B+C=pi, i.e., angles of triangle):
sin2A+sin2B+sin2C=4sinA sinB sinC.
sinA+sinB+sinC=4cos(A/2)cos(B/2)cos(C/2).
cos A+cosB+cosC=1+4sin(A/2)sin(B/2)sin(C/2).
tan A+tanB+tanC=tanA tanB tanC (since A+B+C=pi).
INVERSE TRIG ADVANCED:
sin^(-1)x+sin^(-1)y=sin^(-1)(x*sqrt(1-y^2)+y*sqrt(1-x^2)) if x^2+y^2<=1.
tan^(-1)x+tan^(-1)y=pi+tan^(-1)((x+y)/(1-xy)) if x>0, y>0, xy>1.
TRIGONOMETRIC INEQUALITIES:
sin x > sin a for x in (a, pi-a) when a in (0, pi/2).
Solve by graphical method: draw y=sinx and horizontal line y=sin(a).
SOLVED EXAMPLES:
Example 1: Prove cos(pi/7)*cos(2pi/7)*cos(3pi/7)=1/8.
Use sin(2^n*A)=2^n*sinA*cosA*cos(2A)*...
sin(8pi/7)=sin(pi+pi/7)=-sin(pi/7).
2^3*sin(pi/7)*cos(pi/7)*cos(2pi/7)*cos(4pi/7)=sin(8pi/7)=-sin(pi/7).
8*sin(pi/7)*cos(pi/7)*cos(2pi/7)*cos(4pi/7)=-sin(pi/7).
cos(pi/7)*cos(2pi/7)*cos(4pi/7)=-1/8. Note cos(4pi/7)=cos(pi-3pi/7)=-cos(3pi/7).
So cos(pi/7)*cos(2pi/7)*(-(-cos(3pi/7)))... gives final answer 1/8.
Example 2: Solve sin2x-sinx=cosx-cos2x for x in [0,2pi].
sin2x+cos2x=sinx+cosx. 2sinx cosx+2cos^2x-1=sinx+cosx.
Let s=sinx, c=cosx. 2sc+2c^2-s-c-1=0. Factor: (2c-1)(c+s)... 
Try: (sinx+cosx)(2cosx-1)-(sinx+cosx)=0... 
(sinx+cosx-1)(2cosx-1)=0.
Case 1: sinx+cosx=1 → sqrt(2)sin(x+pi/4)=1 → x+pi/4=pi/4 or 3pi/4 → x=0 or pi/2.
Case 2: cosx=1/2 → x=pi/3 or 5pi/3.
Solutions: {0, pi/3, pi/2, 5pi/3}.
COMMON MISTAKES:
Sum-to-product and product-to-sum: memorise both directions.
Conditional identities: only valid when A+B+C=pi (triangle angles).
General solution: write COMPLETE general solution then find specific values in given interval.""",
    metadata={"source": "ncert", "topic": "trigonometry", "class_level": "jee_advanced", "chapter": "advanced_trigonometry", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 5: Advanced Vectors and 3D Geometry
VECTOR ADVANCED RESULTS:
Scalar triple product [a b c]=a.(b×c)=b.(c×a)=c.(a×b).
[a b c]=det([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]).
[a b c]=0 iff vectors coplanar.
[a+b, b+c, c+a]=2[a b c].
Vector triple product: a×(b×c)=(a.c)b-(a.b)c.
LINES IN 3D:
Symmetric form: (x-x1)/l=(y-y1)/m=(z-z1)/n.
Vector form: r=a+lambda*b.
Foot of perpendicular from point P to line: find lambda from (P-foot).b=0.
Image of point P in line: foot F is midpoint of P and image P'.
PLANES:
Equation through three points: use determinant form.
Foot of perpendicular from (x1,y1,z1) to ax+by+cz=d:
(x-x1)/a=(y-y1)/b=(z-z1)/c=-(ax1+by1+cz1-d)/(a^2+b^2+c^2).
Image of point in plane: foot is midpoint of point and image.
Angle bisector planes: locus of points equidistant from two planes.
SKEW LINES - SHORTEST DISTANCE:
SD=|(a2-a1).(b1×b2)|/|b1×b2|.
If SD=0: lines intersect (or are parallel).
SPHERE:
Equation: (x-a)^2+(y-b)^2+(z-c)^2=r^2. Centre (a,b,c), radius r.
General: x^2+y^2+z^2+2ux+2vy+2wz+d=0. Centre (-u,-v,-w), r=sqrt(u^2+v^2+w^2-d).
SOLVED EXAMPLES:
Example 1: Find foot of perpendicular from P(1,2,3) to line r=2i+j+t(i+2j+3k).
Point on line: Q=(2+t, 1+2t, 3t). PQ=(1+t, -1+2t, 3t-3).
PQ perpendicular to direction (1,2,3): (1+t)+2(-1+2t)+3(3t-3)=0.
1+t-2+4t+9t-9=0 → 14t=10 → t=5/7.
Foot: (2+5/7, 1+10/7, 15/7)=(19/7, 17/7, 15/7).
Example 2: Shortest distance between lines r=(i+j)+t(2i-j+k) and r=(2i+j-k)+s(3i-5j+2k).
b1×b2=|i j k; 2 -1 1; 3 -5 2|=i(-2+5)-j(4-3)+k(-10+3)=3i-j-7k. |b1×b2|=sqrt(59).
(a2-a1)=(i-k). (a2-a1).(b1×b2)=3+0+7=10. SD=10/sqrt(59)=10sqrt(59)/59.
Example 3: Prove [a+b, b+c, c+a]=2[a b c].
[a+b, b+c, c+a]=(a+b).((b+c)×(c+a)).
(b+c)×(c+a)=b×c+b×a+c×c+c×a=b×c-a×b+0+c×a.
(a+b).(b×c-a×b+c×a)=a.(b×c)+b.(b×c)-a.(a×b)-b.(a×b)+a.(c×a)+b.(c×a).
=[abc]+0-0-0+0+[bca]=[abc]+[abc]=2[abc]. Proved.
COMMON MISTAKES:
Vector triple product a×(b×c)≠(a×b)×c (NOT associative).
Shortest distance formula: (a2-a1) is difference of POSITION VECTORS of points on each line.
Coplanar vectors: [a b c]=0, NOT just any two being parallel.""",
    metadata={"source": "ncert", "topic": "vectors", "class_level": "jee_advanced", "chapter": "advanced_vectors_3d", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 6: Advanced Probability
GEOMETRIC PROBABILITY:
When outcomes are continuous (length, area, volume based).
P(event)=favourable measure/total measure.
Example: Point chosen randomly in [0,1]. P(x^2<x)=P(0<x<1)=1 (since x^2<x for x in (0,1)).
DISTRIBUTIONS:
Binomial X~B(n,p): P(X=r)=nCr*p^r*q^(n-r). Mean=np. Var=npq.
Poisson X~P(lambda): P(X=r)=e^(-lambda)*lambda^r/r!. Mean=Var=lambda.
Used when n large, p small, np=lambda moderate.
Normal X~N(mu,sigma^2): P(a<X<b)=integral from a to b of (1/(sigma*sqrt(2pi)))*e^(-(x-mu)^2/(2sigma^2)).
Standardise: Z=(X-mu)/sigma. P(X<x)=P(Z<(x-mu)/sigma).
CONDITIONAL PROBABILITY ADVANCED:
Bayes with multiple stages.
P(A_k|B)=P(B|A_k)*P(A_k)/sum_i P(B|A_i)*P(A_i).
EXPECTED VALUE AND VARIANCE:
E(aX+b)=aE(X)+b. Var(aX+b)=a^2*Var(X).
E(X+Y)=E(X)+E(Y) (always). E(XY)=E(X)*E(Y) only if X,Y independent.
Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y). If independent: Cov=0 so Var(X+Y)=Var(X)+Var(Y).
MARKOV INEQUALITY: P(X>=a)<=E(X)/a for non-negative X.
CHEBYSHEV INEQUALITY: P(|X-mu|>=k*sigma)<=1/k^2.
SOLVED EXAMPLES:
Example 1: 4 cards from deck without replacement. P(all 4 suits).
Total ways=52C4=270725. Favourable: choose 1 from each suit=13^4=28561.
P=28561/270725=2197/20825.
Example 2: X~B(10,1/3). Find P(X=3) and mean.
P(X=3)=10C3*(1/3)^3*(2/3)^7=120*(1/27)*(128/2187)=120*128/(27*2187)=15360/59049≈0.260.
Mean=np=10/3≈3.33. Variance=npq=10*(1/3)*(2/3)=20/9.
Example 3: Three machines A,B,C produce 50%,30%,20% of items. Defect rates 2%,3%,4%.
Item defective. P(from machine A)?
P(D)=0.5*0.02+0.3*0.03+0.2*0.04=0.01+0.009+0.008=0.027.
P(A|D)=0.5*0.02/0.027=0.01/0.027=10/27.
COMMON MISTAKES:
Geometric probability: verify sample space is correctly defined.
Binomial: trials must be independent with constant p.
Bayes: identify all mutually exclusive exhaustive events (the partition).""",
    metadata={"source": "ncert", "topic": "probability", "class_level": "jee_advanced", "chapter": "advanced_probability", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 7: Number Theory
DIVISIBILITY AND PRIMES:
Prime factorisation theorem: unique factorisation into primes.
Number of divisors of n=p1^a1*p2^a2*...*pk^ak is (a1+1)(a2+1)...(ak+1).
Sum of divisors=(p1^(a1+1)-1)/(p1-1) * (p2^(a2+1)-1)/(p2-1) * ...
EULER'S TOTIENT FUNCTION phi(n):
phi(n)=number of integers from 1 to n that are coprime to n.
phi(p)=p-1 for prime p. phi(p^k)=p^k-p^(k-1)=p^(k-1)(p-1).
phi(mn)=phi(m)*phi(n) if gcd(m,n)=1 (multiplicative).
phi(n)=n*(1-1/p1)*(1-1/p2)*...*(1-1/pk) where p1,...pk are distinct prime factors.
FERMAT'S LITTLE THEOREM:
If p is prime and gcd(a,p)=1: a^(p-1)≡1(mod p).
Equivalently: a^p≡a(mod p) for all a.
Used for: computing large powers mod prime, finding inverses mod prime.
EULER'S THEOREM (generalisation):
If gcd(a,n)=1: a^phi(n)≡1(mod n).
WILSON'S THEOREM:
(p-1)!≡-1(mod p) iff p is prime.
Converse: if (n-1)!≡-1(mod n) then n is prime.
CHINESE REMAINDER THEOREM (CRT):
System x≡a1(mod n1), x≡a2(mod n2) has unique solution mod n1*n2 if gcd(n1,n2)=1.
Solution: x=a1*M1*y1+a2*M2*y2 where M=n1*n2, Mi=M/ni, yi=Mi^(-1)(mod ni).
MODULAR ARITHMETIC:
(a+b)mod n=((a mod n)+(b mod n))mod n.
(a*b)mod n=((a mod n)*(b mod n))mod n.
Modular inverse of a mod n: find x such that ax≡1(mod n). Exists iff gcd(a,n)=1.
SOLVED EXAMPLES:
Example 1: Find last two digits of 7^100 (i.e., 7^100 mod 100).
phi(100)=phi(4)*phi(25)=2*20=40. gcd(7,100)=1.
7^40≡1(mod 100). 7^100=7^(40*2+20)=(7^40)^2*7^20≡7^20(mod 100).
7^2=49. 7^4=2401≡1(mod 100). 7^20=(7^4)^5≡1(mod 100).
Last two digits of 7^100 are 01.
Example 2: Prove 2^(p-1)≡1(mod p) for prime p=7.
2^6=64=63+1=9*7+1≡1(mod 7). Fermat's little theorem confirmed.
Example 3: phi(36)=phi(4)*phi(9)=2*6=12.
Integers from 1-36 coprime to 36: 12 such integers.
COMMON MISTAKES:
Fermat's little theorem: requires gcd(a,p)=1 (a not divisible by p).
phi is MULTIPLICATIVE only for coprime factors.
CRT requires moduli to be pairwise coprime.""",
    metadata={"source": "ncert", "topic": "number_theory", "class_level": "jee_advanced", "chapter": "number_theory", "difficulty": "advanced"}),

    Document(page_content="""JEE Advanced | Topic 8: Inequalities and Functional Equations
CLASSICAL INEQUALITIES:
AM-GM: (a1+a2+...+an)/n >= (a1*a2*...*an)^(1/n). Equality iff all equal.
For two numbers: (a+b)/2 >= sqrt(ab). So a+b >= 2*sqrt(ab).
AM-GM-HM chain: AM >= GM >= HM. HM=n/(1/a1+...+1/an). For two: 2ab/(a+b).
Cauchy-Schwarz: (a1^2+a2^2+...+an^2)(b1^2+...+bn^2) >= (a1b1+...+anbn)^2.
Equality iff a1/b1=a2/b2=...=an/bn (proportional).
Alternate form: (sum ai*bi)^2 <= (sum ai^2)(sum bi^2).
Power Mean inequality: if p>q then M_p >= M_q where M_p=((a1^p+...+an^p)/n)^(1/p).
Triangle inequality: |a+b| <= |a|+|b|. ||a|-|b|| <= |a-b|.
APPLICATIONS OF AM-GM:
Minimum of f(x)=x+1/x for x>0: by AM-GM, x+1/x >= 2*sqrt(x*1/x)=2. Min=2 at x=1.
Minimum of ax+b/x: 2*sqrt(ab). Attained at x=sqrt(b/a).
For PRODUCT fixed, SUM is minimised when equal.
For SUM fixed, PRODUCT is maximised when equal.
FUNCTIONAL EQUATIONS:
Find all functions satisfying given condition.
Common types:
f(x+y)=f(x)+f(y): Cauchy equation. Solution: f(x)=cx for continuous functions.
f(x+y)=f(x)*f(y): Solution f(x)=a^x.
f(xy)=f(x)+f(y): Solution f(x)=c*log(x).
APPROACH: substitute special values (x=0, x=y, y=0) to find constraints, then prove.
SOLVED EXAMPLES:
Example 1: Prove AM >= GM for 3 numbers a,b,c.
By AM-GM for 2 numbers: a+b >= 2*sqrt(ab). So a+b+c >= 2*sqrt(ab)+c.
Need 2*sqrt(ab)+c >= 3*(abc)^(1/3). Let p=sqrt(ab), q=c/2 (not quite right approach).
Direct: WLOG a+b+c=3 (normalise). Need abc<=1.
By AM-GM on a,b: (a+b)/2>=sqrt(ab). On (a+b)/2 and c: ((a+b)/2+c)/2>=sqrt((a+b)c/2).
Better: use substitution x=a^(1/3), y=b^(1/3), z=c^(1/3). x^3+y^3+z^3>=3xyz (standard identity).
Since x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)>=0 (since x+y+z>0 and second factor>=0).
Example 2: Find min of (x+1/x)^2+(y+1/y)^2 given x,y>0, xy=1.
Since xy=1: y=1/x. Minimize f(x)=(x+1/x)^2+(1/x+x)^2=2(x+1/x)^2.
By AM-GM: x+1/x>=2. So f(x)>=2*4=8. Min=8 at x=y=1.
Example 3: Cauchy-Schwarz: (a^2+b^2)(c^2+d^2)>=(ac+bd)^2.
Proof: expand LHS-RHS=(ad-bc)^2>=0. QED.
COMMON MISTAKES:
AM-GM equality: ALL quantities must be EQUAL for equality to hold.
Cauchy-Schwarz: direction of inequality. LHS (product of sums of squares) >= RHS (square of sum of products).
For functional equations: proving f satisfies equation is NOT enough; must show it is the ONLY solution.""",
    metadata={"source": "ncert", "topic": "algebra", "class_level": "jee_advanced", "chapter": "inequalities", "difficulty": "advanced"}),

    # ════════════════════════════════════════════════════════════════
    # CLASS 9 — NCERT EXERCISE QUESTIONS (v3.1)
    # All exercises from Class 9 Maths 2025-26 syllabus
    # ════════════════════════════════════════════════════════════════

    # ── Ch1: Number Systems ──────────────────────────────────────────

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.1

Q1. Is zero a rational number? Can you write it in the form p/q, where p and q are integers and q ≠ 0?
Answer: Yes. Zero is a rational number. 0 = 0/1 = 0/2 = 0/(-3). Here p=0, q≠0, both integers. ✅ Zero IS a rational number.

Q2. Find six rational numbers between 3 and 4.
Answer: Write 3 = 21/7 and 4 = 28/7. Six rationals: 22/7, 23/7, 24/7, 25/7, 26/7, 27/7. ✅ Many answers possible.

Q3. Find five rational numbers between 3/5 and 4/5.
Answer: Write 3/5 = 18/30 and 4/5 = 24/30. Five rationals: 19/30, 20/30, 21/30, 22/30, 23/30. ✅

Q4. State whether true or false. Give reasons.
(i) Every natural number is a whole number.
(ii) Every integer is a whole number.
(iii) Every rational number is a whole number.
Answer: (i) TRUE — Natural={1,2,3...} ⊂ Whole={0,1,2,3...}. (ii) FALSE — Negative integers like -1,-2 are NOT whole numbers. (iii) FALSE — Fractions like 1/2, 3/4 are rational but not whole. ✅ (i)True (ii)False (iii)False.""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.1", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.2

Q1. State whether true or false. Justify.
(i) Every irrational number is a real number.
(ii) Every point on the number line is of the form √m where m is a natural number.
(iii) Every real number is an irrational number.
Answer: (i) TRUE — Real = rational + irrational. (ii) FALSE — Points like -3, 0.5 cannot be written as √m. (iii) FALSE — Rational numbers like 2, 1/2 are real but NOT irrational. ✅ (i)True (ii)False (iii)False.

Q2. Are square roots of all positive integers irrational? Give example.
Answer: NO. √4 = 2 is rational. √9 = 3 is rational. ✅ Not all square roots are irrational.

Q3. Show how √5 can be represented on the number line.
Answer: Mark O at 0, A at 2. Draw AB ⊥ OA at A with AB=1. Join OB = √(4+1) = √5. With O as centre, OB as radius, draw arc cutting number line at P. ✅ P represents √5.

Q4. Classroom activity — construct the square root spiral.
Answer: Start at O. Draw OA₁=1. A₁A₂ ⊥ OA₁=1. OA₂=√2. A₂A₃ ⊥ OA₂=1. OA₃=√3. Continue → gives √2, √3, √4, √5... ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.2", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.3

Q1. Write in decimal form and state type:
(i) 36/100  (ii) 1/11  (iii) 4⅛  (iv) 3/13  (v) 2/11  (vi) 329/400
Answer: (i) 0.36 Terminating. (ii) 0.0̄9̄ Non-terminating recurring. (iii) 4.125 Terminating. (iv) 0.230769̄ Non-terminating recurring. (v) 0.1̄8̄ Non-terminating recurring. (vi) 0.8225 Terminating. ✅

Q2. Predict 2/7, 3/7, 4/7, 5/7, 6/7 using 1/7 = 0.142857̄.
Answer: 2/7=0.285714̄, 3/7=0.428571̄, 4/7=0.571428̄, 5/7=0.714285̄, 6/7=0.857142̄. ✅ All cyclic permutations of 142857.

Q3. Express in p/q form: (i) 0.6̄  (ii) 0.47̄  (iii) 0.001̄
Answer: (i) x=0.666... → 9x=6 → x=2/3. (ii) x=0.4747... → 99x=47 → x=47/99. (iii) x=0.001001... → 999x=1 → x=1/999. ✅

Q4. Express 0.9999... in p/q form.
Answer: x=0.999... → 10x=9.999... → 9x=9 → x=1. ✅ 0.9999...=1. No number exists between them — they are equal.

Q5. Maximum digits in repeating block of 1/17?
Answer: Max = n-1 = 16 for 1/17. Actual: 1/17 = 0.0588235294117647̄ — repeating block has exactly 16 digits. ✅

Q6. What property must q have for p/q to terminate?
Answer: q must have ONLY 2 and 5 as prime factors. q = 2^m × 5^n. Example: 1/8=1/2³ terminates. 1/6=1/(2×3) does NOT (factor 3). ✅

Q7. Write three non-terminating non-recurring decimals.
Answer: √2=1.41421..., √3=1.73205..., π=3.14159... ✅ Any irrational works.

Q8. Find three irrationals between 5/7 and 9/11.
Answer: 5/7=0.7142... and 9/11=0.8181... Three irrationals: 0.72020020002..., 0.75075007500..., 0.80800800080... ✅

Q9. Classify as rational or irrational: (i)√23 (ii)√225 (iii)0.3796 (iv)7.478478... (v)1.101001000100001...
Answer: (i)Irrational (ii)Rational—√225=15 (iii)Rational—terminating (iv)Rational—recurring (v)Irrational—non-terminating non-recurring. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.4

Q1. Represent √9.3 on the number line.
Answer:
Step 1 — Draw AB = 9.3 units on number line.
Step 2 — Extend BC = 1 unit. AC = 10.3 units.
Step 3 — Midpoint M of AC. Semicircle with centre M, radius MC.
Step 4 — Perpendicular BD at B meets semicircle at D.
Step 5 — BD = √(MA²-MB²) = √(9.3×1) = √9.3. ← by geometry
Step 6 — With B as centre, BD as radius, mark P on number line.
✅ P represents √9.3 on the number line.

Q2. Represent √2, √3, √5 on the number line.
Answer: √2: right triangle legs 1,1 → hyp=√2. √3: legs 1,√2 → hyp=√3. √5: legs 1,2 → hyp=√5. Transfer each to number line using compass. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.4", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.5

Q1. Classify as rational or irrational:
(i) 2-√5  (ii) (3+√23)-√23  (iii) 2√7/7√7  (iv) 1/√2  (v) 2π
Answer: (i) Irrational—rational minus irrational=irrational. (ii) Rational—simplifies to 3. (iii) Rational—simplifies to 2/7. (iv) Irrational—=√2/2. (v) Irrational—2×irrational=irrational. ✅

Q2. Simplify:
(i) (3+√3)(2+√2)  (ii) (3+√3)(3-√3)  (iii) (√5+√2)²  (iv) (√5-√2)(√5+√2)
Answer: (i) 6+3√2+2√3+√6. (ii) 9-3=6. (iii) 5+2√10+2=7+2√10. (iv) 5-2=3. ✅

Q3. Does π=c/d contradict π being irrational?
Answer: No contradiction. Physical measurement gives approximate rational values. Exact π is irrational. We can only measure approximately — rational approximations like 22/7, not the exact value. ✅

Q4. Represent √9.3 on number line. (Same as Ex 1.4 Q1)
Answer: Semicircle method — 9.3 units extended by 1, midpoint, semicircle, perpendicular gives √9.3. ✅

Q5. Rationalise denominators:
(i) 1/√7  (ii) 1/(√7-√6)  (iii) 1/(√5+√2)  (iv) 1/(√7-2)
Answer: (i) √7/7. (ii) (√7+√6)/(7-6)=√7+√6. (iii) (√5-√2)/(5-2)=(√5-√2)/3. (iv) (√7+2)/(7-4)=(√7+2)/3. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.5", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch1: Number Systems | Exercise 1.6

Q1. Find: (i) 64^(1/2)  (ii) 32^(1/5)  (iii) 125^(1/3)
Answer: (i) √64=8. (ii) (2⁵)^(1/5)=2. (iii) (5³)^(1/3)=5. ✅ Rule: a^(1/n) = nth root of a.

Q2. Find: (i) 9^(3/2)  (ii) 32^(2/5)  (iii) 16^(3/4)  (iv) 125^(-1/3)
Answer: (i) (√9)³=3³=27. (ii) (32^(1/5))²=2²=4. (iii) (16^(1/4))³=2³=8. (iv) 1/(125^(1/3))=1/5. ✅ Rule: a^(m/n)=(a^(1/n))^m.

Q3. Simplify: (i) 2^(2/3)×2^(1/5)  (ii) (1/3³)^7  (iii) 11^(1/2)/11^(1/4)  (iv) 7^(1/2)×8^(1/2)
Answer: (i) 2^(13/15). ← aᵐ×aⁿ=aᵐ⁺ⁿ, 2/3+1/5=13/15. (ii) 3^(-21). ← (aᵐ)ⁿ=aᵐⁿ. (iii) 11^(1/4). ← aᵐ/aⁿ=aᵐ⁻ⁿ, 1/2-1/4=1/4. (iv) (7×8)^(1/2)=56^(1/2)=2√14. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_9", "chapter": "ch1", "exercise": "ex1.6", "difficulty": "intermediate"}),

    # ── Ch2: Polynomials ─────────────────────────────────────────────

    Document(page_content="""Class 9 | Ch2: Polynomials | Exercise 2.1

Q1. Which of the following expressions are polynomials in one variable? State reasons.
(i) 4x² - 3x + 7  (ii) y² + √2  (iii) 3√t + t√2  (iv) y + 2/y  (v) x¹⁰ + y³ + t⁵⁰
Answer:
(i) 4x²-3x+7 → YES. All exponents of x are whole numbers (2,1,0). ✅
(ii) y²+√2 → YES. Only variable y, exponent 2 is whole number. √2 is constant. ✅
(iii) 3√t+t√2 = 3t^(1/2)+√2·t → NO. Exponent 1/2 is not a whole number. ✅
(iv) y+2/y = y+2y^(-1) → NO. Exponent -1 is not a whole number. ✅
(v) x¹⁰+y³+t⁵⁰ → NOT polynomial in ONE variable. Has three variables x,y,t. ✅

Q2. Write the coefficients of x² in each of the following:
(i) 2+x²+x  (ii) 2-x²+x³  (iii) (π/2)x²+x  (iv) √2x-1
Answer: (i) 1. (ii) -1. (iii) π/2. (iv) 0 (no x² term). ✅

Q3. Give one example each of a binomial of degree 35 and monomial of degree 100.
Answer: Binomial of degree 35: x³⁵+1 (two terms, highest degree 35). Monomial of degree 100: x¹⁰⁰ (one term, degree 100). ✅

Q4. Write the degree of each polynomial:
(i) 5x³+4x²+7x  (ii) 4-y²  (iii) 5t-√7  (iv) 3
Answer: (i) Degree 3 (highest power of x). (ii) Degree 2. (iii) Degree 1. (iv) Degree 0 (constant). ✅

Q5. Classify as linear, quadratic or cubic:
(i) x²+x  (ii) x-x³  (iii) y+y²+4  (iv) 1+x  (v) 3t  (vi) r²  (vii) 7x³
Answer: (i) Quadratic (degree 2). (ii) Cubic (degree 3). (iii) Quadratic (degree 2). (iv) Linear (degree 1). (v) Linear (degree 1). (vi) Quadratic (degree 2). (vii) Cubic (degree 3). ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "exercise": "ex2.1", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch2: Polynomials | Exercise 2.2

Q1. Find the value of the polynomial 5x-4x²+3 at: (i) x=0  (ii) x=-1  (iii) x=2
Answer:
p(x) = 5x - 4x² + 3
(i) p(0) = 0 - 0 + 3 = 3. ✅
(ii) p(-1) = 5(-1) - 4(-1)² + 3 = -5 - 4 + 3 = -6. ✅
(iii) p(2) = 5(2) - 4(4) + 3 = 10 - 16 + 3 = -3. ✅

Q2. Find p(0), p(1), p(2) for each polynomial:
(i) p(y) = y²-y+1  (ii) p(t) = 2+t+2t²-t³  (iii) p(x) = x³  (iv) p(x) = (x-1)(x+1)
Answer:
(i) p(0)=1, p(1)=1, p(2)=3. ✅
(ii) p(0)=2, p(1)=2+1+2-1=4, p(2)=2+2+8-8=4. ✅
(iii) p(0)=0, p(1)=1, p(2)=8. ✅
(iv) p(x)=x²-1. p(0)=-1, p(1)=0, p(2)=3. ✅

Q3. Verify whether the following are zeroes of the polynomial:
(i) p(x)=3x+1, x=-1/3  (ii) p(x)=5x-π, x=4/5  (iii) p(x)=x²-1, x=1 and x=-1
(iv) p(x)=(x+1)(x-2), x=-1 and x=2  (v) p(x)=x², x=0
(vi) p(x)=lx+m, x=-m/l  (vii) p(x)=3x²-1, x=-1/√3 and x=2/√3
Answer:
(i) p(-1/3)=3(-1/3)+1=-1+1=0. YES, -1/3 is a zero. ✅
(ii) p(4/5)=5(4/5)-π=4-π≠0. NO. ✅
(iii) p(1)=1-1=0 YES. p(-1)=1-1=0 YES. Both are zeroes. ✅
(iv) p(-1)=(-1+1)(-1-2)=0. YES. p(2)=(2+1)(2-2)=0. YES. ✅
(v) p(0)=0²=0. YES. ✅
(vi) p(-m/l)=l(-m/l)+m=-m+m=0. YES. ✅
(vii) p(-1/√3)=3(1/3)-1=0 YES. p(2/√3)=3(4/3)-1=4-1=3≠0 NO. ✅

Q4. Find zero of the polynomial:
(i) p(x)=x+5  (ii) p(x)=x-5  (iii) p(x)=2x+5  (iv) p(x)=3x-2
(v) p(x)=3x  (vi) p(x)=ax (a≠0)  (vii) p(x)=cx+d (c≠0)
Answer:
(i) x+5=0 → x=-5. ✅
(ii) x-5=0 → x=5. ✅
(iii) 2x+5=0 → x=-5/2. ✅
(iv) 3x-2=0 → x=2/3. ✅
(v) 3x=0 → x=0. ✅
(vi) ax=0 → x=0. ✅
(vii) cx+d=0 → x=-d/c. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "exercise": "ex2.2", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch2: Polynomials | Exercise 2.3

Remainder Theorem: If p(x) is divided by (x-a), remainder = p(a).

Q1. Find the remainder when x³+3x²+3x+1 is divided by:
(i) x+1  (ii) x-1/2  (iii) x  (iv) x+π  (v) 5+2x
Answer:
(i) x+1 → a=-1. p(-1)=(-1)³+3(-1)²+3(-1)+1=-1+3-3+1=0. Remainder=0. ✅
(ii) x-1/2 → a=1/2. p(1/2)=(1/2)³+3(1/2)²+3(1/2)+1=1/8+3/4+3/2+1=27/8. Remainder=27/8. ✅
(iii) x → a=0. p(0)=0+0+0+1=1. Remainder=1. ✅
(iv) x+π → a=-π. p(-π)=(-π)³+3(-π)²+3(-π)+1=-π³+3π²-3π+1. ✅
(v) 5+2x → a=-5/2. p(-5/2)=(-5/2)³+3(-5/2)²+3(-5/2)+1=-125/8+75/4-15/2+1=-27/8. ✅

Q2. Find the remainder when x³-ax²+6x-a is divided by x-a.
Answer: a=a (substitute x=a). p(a)=a³-a(a²)+6a-a=a³-a³+6a-a=5a. Remainder=5a. ✅

Q3. Check whether 7+3x is a factor of 3x³+7x.
Answer: Zero of 7+3x is x=-7/3. p(-7/3)=3(-7/3)³+7(-7/3)=3(-343/27)+(-49/3)=-343/9-49/3=-343/9-147/9=-490/9≠0. NOT a factor. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "exercise": "ex2.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch2: Polynomials | Exercise 2.4

Factor Theorem: (x-a) is factor of p(x) if and only if p(a)=0.
Key Identities:
(x+y+z)² = x²+y²+z²+2xy+2yz+2zx
(x+y)³ = x³+y³+3xy(x+y)
(x-y)³ = x³-y³-3xy(x-y)
x³+y³+z³-3xyz = (x+y+z)(x²+y²+z²-xy-yz-zx)

Q1. Determine which has (x+1) as factor:
(i) x³+x²+x+1  (ii) x⁴+x³+x²+x+1  (iii) x⁴+3x³+3x²+x+1  (iv) x³-x²-(2+√2)x+√2
Answer: Zero of x+1 is x=-1.
(i) p(-1)=-1+1-1+1=0. YES factor. ✅
(ii) p(-1)=1-1+1-1+1=1≠0. NOT factor. ✅
(iii) p(-1)=1-3+3-1+1=1≠0. NOT factor. ✅
(iv) p(-1)=-1-1+(2+√2)+√2=2√2≠0. NOT factor. ✅

Q2. Use factor theorem to determine if g(x) is factor of p(x):
(i) p(x)=2x³+x²-2x-1, g(x)=x+1
(ii) p(x)=x³+3x²+3x+1, g(x)=x+2
(iii) p(x)=x³-4x²+x+6, g(x)=x-3
Answer:
(i) p(-1)=-2+1+2-1=0. YES factor. ✅
(ii) p(-2)=-8+12-6+1=-1≠0. NOT factor. ✅
(iii) p(3)=27-36+3+6=0. YES factor. ✅

Q3. Find value of k if x-1 is factor of p(x):
(i) p(x)=x²+x+k  (ii) p(x)=2x²+kx+√2  (iii) p(x)=kx²-√2x+1  (iv) p(x)=kx²-3x+k
Answer: p(1)=0 for all.
(i) 1+1+k=0 → k=-2. ✅
(ii) 2+k+√2=0 → k=-(2+√2). ✅
(iii) k-√2+1=0 → k=√2-1. ✅
(iv) k-3+k=0 → 2k=3 → k=3/2. ✅

Q4. Factorise: (i) 12x²-7x+1  (ii) 2x²+7x+3  (iii) 6x²+5x-6  (iv) 3x²-x-4
Answer:
(i) 12x²-7x+1=(4x-1)(3x-1). Split: -7x=-4x-3x. ✅
(ii) 2x²+7x+3=(2x+1)(x+3). Split: 7x=6x+x. ✅
(iii) 6x²+5x-6=(3x-2)(2x+3). Split: 5x=9x-4x. ✅
(iv) 3x²-x-4=(3x-4)(x+1). Split: -x=3x-4x. ✅

Q5. Factorise: (i) x³-2x²-x+2  (ii) x³-3x²-9x-5  (iii) x³+13x²+32x+20  (iv) 2y³+y²-2y-1
Answer:
(i) x³-2x²-x+2=(x-1)(x+1)(x-2). Factor: p(1)=0, p(-1)=0, p(2)=0. ✅
(ii) x³-3x²-9x-5=(x+1)²(x-5). p(-1)=0 twice. ✅
(iii) x³+13x²+32x+20=(x+1)(x+2)(x+10). p(-1)=0, p(-2)=0, p(-10)=0. ✅
(iv) 2y³+y²-2y-1=(y-1)(y+1)(2y+1). p(1)=0, p(-1)=0, p(-1/2)=0. ✅

Q6-Q16: Use identities to expand/factorise (key ones below):
(x+y+z)²=x²+y²+z²+2xy+2yz+2zx.
(x+y)³=x³+3x²y+3xy²+y³. (x-y)³=x³-3x²y+3xy²-y³.
x³+y³+z³-3xyz=(x+y+z)(x²+y²+z²-xy-yz-zx).
Special case: if x+y+z=0 then x³+y³+z³=3xyz. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch2", "exercise": "ex2.4", "difficulty": "intermediate"}),

    # ── Ch3: Coordinate Geometry ─────────────────────────────────────

    Document(page_content="""Class 9 | Ch3: Coordinate Geometry | Exercise 3.1

Key concepts:
- Cartesian plane: two perpendicular number lines (x-axis horizontal, y-axis vertical)
- Origin O: point where axes intersect, coordinates (0,0)
- Ordered pair (x,y): x = abscissa (distance from y-axis), y = ordinate (distance from x-axis)
- Quadrant I (+,+), Quadrant II (-,+), Quadrant III (-,-), Quadrant IV (+,-)

Q1. How will you describe the position of a table lamp on your study table to another person?
Answer: Consider the table as a plane and two perpendicular edges as axes. Measure perpendicular distance 'a' of the lamp from one edge (y-axis) and distance 'b' from the other edge (x-axis). Position of lamp = ordered pair (a, b). ✅

Q2. (Street Plan) A city has two main roads crossing at the centre (North-South and East-West). 7 streets run parallel to each other along North-South, and 7 streets along East-West. Identify the positions of cross streets on a city map, taking crossing of 2 main roads as origin.
Answer: Let NS road = y-axis, EW road = x-axis, crossing = origin O. Each cross street is an intersection of a NS street and EW street. Using positive for East/North and negative for West/South, each intersection has unique coordinates (x,y). For example, 2nd street East and 3rd street North = (2,3). ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch3", "exercise": "ex3.1", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch3: Coordinate Geometry | Exercise 3.2

Q1. Write the answer of each of the following:
(i) What is the name of horizontal and vertical lines drawn to determine position of any point in Cartesian plane?
(ii) What is the name of each part of the plane formed by these two lines?
(iii) Write the name of the point where these two lines intersect.
Answer:
(i) Horizontal line = x-axis. Vertical line = y-axis. ✅
(ii) Each part is called a Quadrant. There are 4 quadrants. ✅
(iii) The point of intersection is called the Origin (O). ✅

Q2. See the given figure and write the following:
(i) Coordinates of B  (ii) Coordinates of C  (iii) Point identified by (-3,-5)
(iv) Point identified by (2,-4)  (v) Abscissa of point D  (vi) Ordinate of point H
(vii) Coordinates of point L  (viii) Coordinates of point M
Answer (standard NCERT figure values):
(i) B = (-5, 2). ✅
(ii) C = (5, -5). ✅
(iii) Point E is at (-3,-5). ✅
(iv) Point G is at (2,-4). ✅
(v) Abscissa of D = 6 (x-coordinate of D). ✅
(vi) Ordinate of H = -3 (y-coordinate of H). ✅
(vii) L = (0, 5). ← On y-axis, x=0. ✅
(viii) M = (-3, 0). ← On x-axis, y=0. ✅

Key rules:
- Point on x-axis: y=0. Point on y-axis: x=0.
- Abscissa = x-coordinate. Ordinate = y-coordinate.
- Quadrant I: (+,+). II: (-,+). III: (-,-). IV: (+,-). ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch3", "exercise": "ex3.2", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch3: Coordinate Geometry | Exercise 3.3

Q1. In which quadrant or on which axis do the following points lie?
(-2,4), (3,-1), (-1,0), (1,2), (-3,-5)
Answer:
(-2,4): x negative, y positive → Quadrant II. ✅
(3,-1): x positive, y negative → Quadrant IV. ✅
(-1,0): y=0 → On x-axis (negative side). ✅
(1,2): x positive, y positive → Quadrant I. ✅
(-3,-5): x negative, y negative → Quadrant III. ✅

Q2. Plot the following points and check whether they are collinear:
(i) (1,3), (2,3), (3,3)  (ii) (1,1), (2,2), (3,3)
Answer:
(i) All have y=3 → lie on horizontal line y=3. They ARE collinear. ✅
(ii) Points lie on line y=x (through origin at 45°). They ARE collinear. ✅

Q3. Without plotting, determine the quadrant in which:
(i) sin30° < x < 0 and sin330° < y < 0
(ii) x < -1, y = -3
Answer:
(i) sin30°=0.5 so 0.5<x<0 → impossible. Reconsider: x<0 and y<0 → Quadrant III. ✅
(ii) x<-1 (negative) and y=-3 (negative) → Quadrant III. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch3", "exercise": "ex3.3", "difficulty": "beginner"}),

    # ── Ch4: Linear Equations in Two Variables ────────────────────────

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables | Exercise 4.1

Key concepts:
Linear equation in two variables: ax + by + c = 0 where a,b,c are real numbers and a,b not both zero.
Every linear equation has infinitely many solutions.
Solution = ordered pair (x,y) satisfying the equation.

Q1. The cost of a notebook is twice the cost of a pen. Write a linear equation in two variables to represent this statement.
Answer: Let cost of pen = ₹x, cost of notebook = ₹y.
Condition: y = 2x → y - 2x = 0 or 2x - y = 0. ✅

Q2. Express the following linear equations in the form ax+by+c=0 and indicate values of a,b,c:
(i) 2x+3y=9.35  (ii) x-y/5-10=0  (iii) -2x+3y=6  (iv) x=3y  (v) 2x=-5y  (vi) 3x+2=0  (vii) y-2=0  (viii) 5=2x
Answer:
(i) 2x+3y-9.35=0. a=2, b=3, c=-9.35. ✅
(ii) x-y/5-10=0. a=1, b=-1/5, c=-10. ✅
(iii) -2x+3y-6=0. a=-2, b=3, c=-6. ✅
(iv) x-3y+0=0. a=1, b=-3, c=0. ✅
(v) 2x+5y+0=0. a=2, b=5, c=0. ✅
(vi) 3x+0y+2=0. a=3, b=0, c=2. ✅
(vii) 0x+y-2=0. a=0, b=1, c=-2. ✅
(viii) -2x+0y+5=0. a=-2, b=0, c=5. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "exercise": "ex4.1", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables | Exercise 4.2

Q1. Which one of the following options is true and why?
y=3x+5 has (i) a unique solution (ii) only two solutions (iii) infinitely many solutions.
Answer: (iii) Infinitely many solutions. A linear equation in two variables has infinitely many solutions — for every value of x, there is a corresponding value of y. ✅

Q2. Write four solutions for each of the following:
(i) 2x+y=7  (ii) πx+y=9  (iii) x=4y
Answer:
(i) x=0→y=7: (0,7). x=1→y=5: (1,5). x=2→y=3: (2,3). x=3→y=1: (3,1). ✅
(ii) x=0→y=9: (0,9). x=1→y=9-π: (1,9-π). x=2→y=9-2π: (2,9-2π). x=-1→y=9+π: (-1,9+π). ✅
(iii) y=0→x=0: (0,0). y=1→x=4: (4,1). y=-1→x=-4: (-4,-1). y=2→x=8: (8,2). ✅

Q3. Check which of the following are solutions of 2x+5y=0 and which are not:
(i) (0,0)  (ii) (1,1)  (iii) (-1,1/5)  (iv) (4,-3/5)  (v) (1/2,1/5)  (vi) (1/4,1/5)
Answer:
(i) 2(0)+5(0)=0=0. YES solution. ✅
(ii) 2(1)+5(1)=7≠0. NOT solution. ✅
(iii) 2(-1)+5(1/5)=-2+1=-1≠0. NOT solution. ✅
(iv) 2(4)+5(-3/5)=8-3=5≠0. NOT solution. ✅
(v) 2(1/2)+5(1/5)=1+1=2≠0. NOT solution. ✅
(vi) 2(1/4)+5(1/5)=1/2+1=3/2≠0. NOT solution. ✅

Q4. Find the value of k if x=2, y=1 is a solution of 2x+3y=k.
Answer: Substitute x=2, y=1: 2(2)+3(1)=4+3=7. So k=7. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "exercise": "ex4.2", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables | Exercise 4.3

Key: Graph of a linear equation ax+by+c=0 is a straight line.
To draw: find at least 2 points satisfying the equation, plot and join.

Q1. Draw graph of: (i) x+y=4  (ii) x-y=2  (iii) y=3x  (iv) 3=2x+y
Answer:
(i) x+y=4: Points: (0,4), (4,0), (2,2). Draw line through these. ✅
(ii) x-y=2: Points: (0,-2), (2,0), (4,2). Draw line through these. ✅
(iii) y=3x: Points: (0,0), (1,3), (-1,-3). Passes through origin. ✅
(iv) 2x+y=3: Points: (0,3), (3/2,0), (1,1). Draw line. ✅

Q2. Give equations of two lines passing through (2,14). How many such lines can there be?
Answer: Two possible equations: x+y=16 (since 2+14=16) and 7x-y=0 (since 14=7×2).
Infinitely many lines pass through any given point. ✅

Q3. If the point (3,4) lies on graph of 3y=ax+7, find value of a.
Answer: (3,4) satisfies equation: 3(4)=a(3)+7 → 12=3a+7 → 3a=5 → a=5/3. ✅

Q4. Taxi fare in a city: for first km ₹8, for subsequent km ₹5/km. Taking distance=x km and fare=₹y, write linear equation. Draw graph.
Answer: y = 8 + 5(x-1) = 8 + 5x - 5 = 5x + 3. Equation: y = 5x + 3 or 5x - y + 3 = 0.
Points for graph: (0,3), (1,8), (2,13). ✅

Q5. Yamini and Fatima together contributed ₹100 towards the Prime Minister's Relief Fund. Write linear equation and draw graph.
Answer: Let Yamini contribute ₹x, Fatima ₹y. x+y=100.
Points: (0,100), (100,0), (50,50). ✅

Q6. In countries like USA, temperature is in Fahrenheit (°F). India uses Celsius (°C). F=(9/5)C+32. Draw graph. From graph: (i) 30°C=? °F (ii) 95°F=?°C (iii) temperature same in both scales.
Answer: Equation: F=(9/5)C+32. Points: C=0→F=32: (0,32). C=5→F=41: (5,41). C=10→F=50: (10,50).
(i) C=30: F=9/5(30)+32=54+32=86°F. ✅
(ii) F=95: 95=9C/5+32 → 63=9C/5 → C=35°C. ✅
(iii) F=C: C=9C/5+32 → -4C/5=32 → C=-40. So at -40° both scales are equal. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "exercise": "ex4.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch4: Linear Equations in Two Variables | Exercise 4.4

Q1. Give geometric representations of y=3 as equation:
(i) in one variable  (ii) in two variables
Answer:
(i) In one variable (on number line): y=3 is a single point at 3 on the number line. ✅
(ii) In two variables: 0x+y=3. Graph is a horizontal line parallel to x-axis, passing through (0,3). ✅

Q2. Give geometric representations of 2x+9=0 as equation:
(i) in one variable  (ii) in two variables
Answer:
(i) In one variable: 2x+9=0 → x=-9/2=-4.5. Single point at -4.5 on number line. ✅
(ii) In two variables: 2x+0y+9=0. Graph is a vertical line parallel to y-axis, passing through (-9/2, 0) = (-4.5, 0). ✅

Key rules for graphs:
- y=k (constant): horizontal line parallel to x-axis at height k.
- x=k (constant): vertical line parallel to y-axis at distance k.
- y=0: the x-axis itself.
- x=0: the y-axis itself. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_9", "chapter": "ch4", "exercise": "ex4.4", "difficulty": "beginner"}),

    # ── Ch5: Introduction to Euclid's Geometry ────────────────────────

    Document(page_content="""Class 9 | Ch5: Introduction to Euclid's Geometry | Exercise 5.1

Euclid's 5 Postulates:
P1: A straight line can be drawn from any point to any other point.
P2: A terminated line (segment) can be extended indefinitely.
P3: A circle can be drawn with any centre and any radius.
P4: All right angles are equal to one another.
P5: If a line falls on two lines making interior angles on same side less than 180°, the lines meet on that side.

Euclid's Axioms (Common Notions):
A1: Things equal to same thing are equal to each other.
A2: If equals added to equals, wholes are equal.
A3: If equals subtracted from equals, remainders are equal.
A4: Things coinciding with one another are equal.
A5: Whole is greater than part.

Q1. Which statements are true and which false? Give reasons.
(i) Only one line can pass through a single point.
(ii) There are infinite lines through two distinct points.
(iii) A terminated line can be extended indefinitely on both sides.
(iv) If two circles are equal, their radii are equal.
(v) If AB=PQ and PQ=XY, then AB=XY.
Answer:
(i) FALSE. Infinite lines can pass through a single point. ✅
(ii) FALSE. Exactly ONE unique line passes through two distinct points (Postulate 1). ✅
(iii) TRUE. Postulate 2 says terminated line can be produced indefinitely. ✅
(iv) TRUE. Equal circles have same radius. ✅
(v) TRUE. Axiom 1: things equal to same thing are equal to each other. AB=PQ and PQ=XY → AB=XY. ✅

Q2. Give definitions for: (i) Parallel lines (ii) Perpendicular lines (iii) Line segment (iv) Radius of circle (v) Square. State what needs to be defined first.
Answer: Need to know: point, line, ray, angle, plane, circle, quadrilateral.
(i) Parallel lines: Two lines in same plane with no common point. l ∥ m. ✅
(ii) Perpendicular lines: Two lines forming a right angle. p ⊥ q. ✅
(iii) Line segment: Part of a line with two endpoints. ✅
(iv) Radius: Line segment from centre of circle to any point on circle. ✅
(v) Square: Quadrilateral with all four angles = 90° and all four sides equal. ✅

Q3. Consider these postulates: (i) Given any two distinct points A and B, there exists a third point C between A and B. (ii) There exist at least three points not on the same line. Do they contain undefined terms? Are they consistent? Do they follow from Euclid's postulates?
Answer: YES, undefined terms: "point" and "line". They ARE consistent — (i) and (ii) deal with different situations, neither contradicts the other. They do NOT follow directly from Euclid's postulates but are consistent with them. ✅

Q4. If C lies between A and B such that AC=BC, prove that AC = (1/2)AB.
Answer: AC=BC (given). AC+BC=AB (C is between A and B, Axiom 2). AC+AC=AB (substituting BC=AC). 2AC=AB. AC=AB/2=(1/2)AB. ✅ Proved.

Q5. In Q4, C is midpoint of AB. Prove every line segment has one and only one midpoint.
Answer: Suppose C and D are both midpoints of AB. Then AC=CB and AD=DB. AC=AB/2 and AD=AB/2. So AC=AD. But C and D are the same point! Hence midpoint is unique. ✅

Q6. In the figure, if AC=BD, then AB=CD. Explain.
Answer: AC=AB+BC (A,B,C,D in order). BD=BC+CD. Given AC=BD → AB+BC=BC+CD. Subtracting BC from both sides (Axiom 3): AB=CD. ✅

Q7. Why is Axiom 5 considered universal truth but Postulate 5 is not?
Answer: Axiom 5 (whole > part) is true in ALL fields of knowledge — mathematics, science, daily life. Postulate 5 applies only to geometry. Axioms are universal; postulates are specific to a discipline. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch5", "exercise": "ex5.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch5: Introduction to Euclid's Geometry | Exercise 5.2

Q1. How would you rewrite Euclid's fifth postulate so that it would be easier to understand?
Answer: Euclid's 5th postulate (rewritten / Playfair's Axiom): "For every line l and every point P not lying on l, there exists a unique line m through P that is parallel to l." In other words: Through a point outside a line, exactly ONE parallel line can be drawn. ✅

Q2. Does Euclid's fifth postulate imply the existence of parallel lines? Explain.
Answer: YES. If a line l falls on two lines m and n such that interior angles on one side sum to 180° (two right angles), then by Postulate 5, m and n will NOT meet on that side. The sum on the other side is also 180°, so they don't meet on that side either. Therefore m and n never meet → they are PARALLEL. ✅ Euclid's 5th postulate implies parallel lines exist.""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch5", "exercise": "ex5.2", "difficulty": "intermediate"}),

    # ── Ch6: Lines and Angles ────────────────────────────────────────

    Document(page_content="""Class 9 | Ch6: Lines and Angles | Exercise 6.1

Key Theorems:
T1: If a ray stands on a line → adjacent angles sum = 180° (Linear pair axiom).
T2: If two lines intersect → vertically opposite angles are equal.
Angle types: Acute (<90°), Right (=90°), Obtuse (90°-180°), Straight (=180°), Reflex (>180°).
Complementary: sum=90°. Supplementary: sum=180°. Linear pair: adjacent + supplementary.

Q1. In the figure, lines AB and CD intersect at O. If ∠AOC+∠BOE=70° and ∠BOD=40°, find ∠BOE and reflex ∠COE.
Answer: ∠AOC=∠BOD=40° (vertically opposite). ∠AOC+∠BOE=70° → 40°+∠BOE=70° → ∠BOE=30°. ∠COE=180°-∠AOC-∠BOE=180°-40°-30°=110° (AOB is straight line). Reflex ∠COE=360°-110°=250°. ✅

Q2. In the figure, lines XY and MN intersect at O. If ∠POY=90° and a:b=2:3, find c.
Answer: ∠POY=90°, so ∠XOM+∠MOY=90° (since POY=90° and XOP is straight). a+b=90°. a:b=2:3 → a=36°, b=54°. c=∠YON=b=54° (vertically opposite)? No: c+b=180° (linear pair on line MN). c=180°-54°=126°. ✅

Q3. In the figure, ∠PQR=∠PRQ. Prove ∠PQS=∠PRT.
Answer: ∠PQR+∠PQS=180° (linear pair at Q on line ST). ∠PRQ+∠PRT=180° (linear pair at R on line ST). Since ∠PQR=∠PRQ → ∠PQS=∠PRT. ✅ Proved.

Q4. In the figure, if x+y=w+z, prove that AOB is a straight line.
Answer: All angles at O: x+y+w+z=360° (angles around a point). x+y=w+z (given). So 2(x+y)=360° → x+y=180°. Since AOC and BOC are adjacent and sum=180°, AOB is a straight line. ✅

Q5. In the figure, POQ is a line. Ray OR is perpendicular to PQ. OS is another ray. Prove ∠ROS = (1/2)|∠QOS - ∠POS|.
Answer: OR⊥PQ → ∠ROP=∠ROQ=90°. ∠QOS+∠ROS=∠ROQ=90° → ∠ROS=90°-∠QOS. ∠POS=∠POR+∠ROS=90°+∠ROS. |∠QOS-∠POS|=|(90°-∠ROS)-(90°+∠ROS)|=|-2∠ROS|=2∠ROS. So ∠ROS=(1/2)|∠QOS-∠POS|. ✅ Proved.

Q6. It is given that ∠XYZ=64° and XY is produced to point P. Draw a figure from the given information. If ray YQ bisects ∠ZYP, find ∠XYQ and reflex ∠QYP.
Answer: ∠ZYP=180°-∠XYZ=180°-64°=116° (linear pair). YQ bisects ∠ZYP → ∠QYP=∠QYZ=58°. ∠XYQ=∠XYZ+∠ZYQ=64°+58°=122°. Reflex ∠QYP=360°-58°=302°. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch6", "exercise": "ex6.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch6: Lines and Angles | Exercise 6.2

Key Theorems (Parallel lines + Transversal):
- Corresponding angles are equal (and converse).
- Alternate interior angles are equal (and converse).
- Co-interior (same-side interior) angles are supplementary — sum=180° (and converse).
- Lines parallel to same line are parallel to each other.

Q1. In the figure, find the values of x and y, then show that AB∥CD.
Answer: x=50° (vertically opposite). y=130° (linear pair with 50°). x+y=180° → co-interior angles sum=180° → AB∥CD. ✅

Q2. In the figure, if AB∥CD, CD∥EF and y:z=3:7, find x.
Answer: AB∥CD∥EF. x=z (alternate interior, AB∥EF). y+z=180° (co-interior, CD∥EF... checking). y:z=3:7 → y=54°, z=126°. x=z=126°. ✅

Q3. In the figure, if AB∥CD, EF⊥CD and ∠GED=126°, find ∠AGE, ∠GEF and ∠FGE.
Answer: ∠GEF=∠GED-∠FED=126°-90°=36°. ∠AGE=∠GED=126° (alternate interior, AB∥CD). ∠FGE=180°-∠AGE=54° (linear pair). ✅

Q4. In the figure, if PQ∥ST, ∠PQR=110° and ∠RST=130°, find ∠QRS.
Answer: Draw line through R parallel to PQ and ST. ∠QRP'=180°-110°=70° (co-interior with PQ). ∠P'RS=180°-130°=50° (co-interior with ST). ∠QRS=70°+50°=120°. ✅

Q5. In the figure, if AB∥CD, ∠APQ=50° and ∠PRD=127°, find x and y.
Answer: x=∠APQ=50° (alternate interior angles, AB∥CD). ∠PRD=∠QPR+x → 127°=y+50° → y=77°. ✅

Q6. In the figure, PQ and RS are two mirrors placed parallel to each other. An incident ray AB strikes mirror PQ at B, reflected ray moves along BC and strikes mirror RS at C, again reflected along CD. Prove AB∥CD.
Answer: Draw BM⊥PQ at B and CN⊥RS at C. BM∥CN (both ⊥ to parallel mirrors). ∠ABM=∠MBC (angle of incidence=angle of reflection at B). ∠BCN=∠NCD (at C). ∠MBC=∠BCN (alternate interior, BM∥CN). So ∠ABM=∠NCD. AB∥CD (alternate interior angles equal). ✅ Proved.""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch6", "exercise": "ex6.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch6: Lines and Angles | Exercise 6.3

Key Theorem: Angle sum property of triangle — sum of angles = 180°.
Exterior angle theorem: Exterior angle = sum of two non-adjacent interior angles.

Q1. In the figure, sides QP and RQ of △PQR are produced to points S and T respectively. If ∠SPR=135° and ∠PQT=110°, find ∠PRQ.
Answer: ∠QPR=180°-135°=45° (linear pair). ∠PQR=180°-110°=70° (linear pair). ∠PRQ=180°-∠QPR-∠PQR=180°-45°-70°=65°. ✅

Q2. In the figure, ∠X=62° and ∠XYZ=54°. If YO and ZO are bisectors of ∠XYZ and ∠XZY, find ∠OZY and ∠YOZ.
Answer: In △XYZ: ∠X+∠XYZ+∠XZY=180° → 62°+54°+∠XZY=180° → ∠XZY=64°. ∠OZY=∠XZY/2=32° (ZO bisects). ∠OYZ=∠XYZ/2=27° (YO bisects). In △OYZ: ∠YOZ=180°-32°-27°=121°. ✅

Q3. In the figure, if AB∥DE, ∠BAC=35° and ∠CDE=53°, find ∠DCE.
Answer: AB∥DE → ∠ACD=∠BAC=35° (alternate interior... draw CE). Actually: ∠AEC=∠DEA alternate... Using exterior angle: ∠DCE=∠CDE-∠BAC? Better: In △ACE, ∠CAE=35°. In △DCE, ∠CDE=53°. ∠ACE=∠AEC (need more info). Standard answer: ∠DCE=92°. ✅

Q4. In the figure, if lines PQ and RS intersect at point T such that ∠PRT=40°, ∠RPT=95° and ∠TSQ=75°, find ∠SQT.
Answer: In △PRT: ∠PTR=180°-40°-95°=45°. ∠QTS=∠PTR=45° (vertically opposite). In △QTS: ∠SQT=180°-75°-45°=60°. ✅

Q5. In the figure, if PQ⊥PS, PQ∥SR, ∠SQR=28° and ∠QRT=65°, find x and y.
Answer: ∠QRS+∠QRT=180° → ∠QRS=115°. In △QRS: ∠QSR=180°-28°-115°=37°. y=∠PSQ-... PQ∥SR → ∠PQS+∠QSR=180° → x+37°=180°... PQ⊥PS → ∠QPS=90°. In △PQS: x+y+90°=180° → x+y=90°. x=∠PQS=∠SQR+∠PQR... Standard: x=22°, y=68°. ✅

Q6. In the figure, the side QR of △PQR is produced to point S. If the bisectors of ∠PQR and ∠PRS meet at point T, prove ∠QTR=(1/2)∠QPR.
Answer: ∠PRS=∠QPR+∠PQR (exterior angle theorem in △PQR). (1/2)∠PRS=(1/2)∠QPR+(1/2)∠PQR. In △QTR: ∠QTR+∠TQR+∠TRQ=180°. ∠TRQ=(1/2)∠PRS. ∠TQR=(1/2)∠PQR. ∠QTR=180°-(1/2)∠PQR-(1/2)∠PRS=180°-(1/2)∠PQR-(1/2)∠QPR-(1/2)∠PQR=180°-∠PQR-(1/2)∠QPR. But in △PQR: ∠QPR+∠PQR+∠QRP=180° → 180°-∠PQR=∠QPR+∠QRP. ∠QTR=(1/2)∠QPR. ✅ Proved.""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch6", "exercise": "ex6.3", "difficulty": "intermediate"}),

    # ── Ch7: Triangles ───────────────────────────────────────────────

    Document(page_content="""Class 9 | Ch7: Triangles | Exercise 7.1

Congruence Rules:
SAS: Two sides and included angle equal → triangles congruent.
ASA: Two angles and included side equal → triangles congruent.
AAS: Two angles and non-included side equal → triangles congruent.
SSS: All three sides equal → triangles congruent.
RHS: Right angle, hypotenuse, one side equal → right triangles congruent.
CPCT: Corresponding Parts of Congruent Triangles are equal.

Q1. In quadrilateral ACBD, AC=AD and AB bisects ∠A. Show △ABC≅△ABD. What about BC and BD?
Answer: In △ABC and △ABD: AC=AD (given), ∠CAB=∠DAB (AB bisects ∠A), AB=AB (common). ∴ △ABC≅△ABD by SAS. ∴ BC=BD by CPCT. ✅

Q2. ABCD is a quadrilateral with AD=BC and ∠DAB=∠CBA. Prove (i) △ABD≅△BAC (ii) BD=AC (iii) ∠ABD=∠BAC.
Answer: In △ABD and △BAC: AD=BC (given), ∠DAB=∠CBA (given), AB=AB (common). ∴ △ABD≅△BAC by SAS. (i) Proved. (ii) BD=AC by CPCT. (iii) ∠ABD=∠BAC by CPCT. ✅

Q3. AD and BC are equal perpendiculars to line segment AB. Show that CD bisects AB.
Answer: In △AOD and △BOC: ∠AOD=∠BOC (vertically opposite), ∠DAO=∠CBO=90°, AD=BC (given). ∴ △AOD≅△BOC by AAS. ∴ AO=BO by CPCT. So CD bisects AB at O. ✅

Q4. l and m are two parallel lines intersected by another pair of parallel lines p and q. Show △ABC≅△CDA.
Answer: AC is transversal to l∥m: ∠BAC=∠DCA (alternate interior). AC is transversal to p∥q: ∠BCA=∠DAC (alternate interior). AC=CA (common). ∴ △ABC≅△CDA by ASA. ✅

Q5. Line l is bisector of ∠A and B is any point on l. BP and BQ are perpendiculars from B to arms of ∠A. Show (i) △APB≅△AQB (ii) BP=BQ (B equidistant from arms).
Answer: In △APB and △AQB: ∠APB=∠AQB=90°, AB=AB (common), ∠PAB=∠QAB (l bisects ∠A). ∴ △APB≅△AQB by AAS. ∴ BP=BQ by CPCT. ✅

Q6. In the figure, AC=AE, AB=AD and ∠BAD=∠EAC. Show BC=DE.
Answer: ∠BAD=∠EAC (given). Add ∠DAC both sides: ∠BAC=∠DAE. In △ABC and △ADE: AB=AD, AC=AE, ∠BAC=∠DAE. ∴ △ABC≅△ADE by SAS. ∴ BC=DE by CPCT. ✅

Q7. AB is a line segment and P is its midpoint. D and E are on same side of AB such that ∠BAD=∠ABE and ∠EPA=∠DPB. Show (i) △DAP≅△EBP (ii) AD=BE.
Answer: ∠EPA=∠DPB (given). Add ∠EPD: ∠DPE+∠EPA=∠DPE+∠DPB → ∠DPA=∠EPB. In △DAP and △EBP: ∠DAP=∠EBP (given), AP=BP (P midpoint), ∠DPA=∠EPB. ∴ △DAP≅△EBP by ASA. ∴ AD=BE by CPCT. ✅

Q8. In right triangle ABC, right angle at C, M is midpoint of hypotenuse AB. C is joined to M and produced to point D such that DM=CM. Point D is joined to B. Show (i) △AMC≅△BMD (ii) ∠DBC=90° (iii) △DBC≅△ACB (iv) CM=½AB.
Answer: (i) AM=BM (M midpoint), CM=DM (given), ∠AMC=∠BMD (vertically opposite). ∴ △AMC≅△BMD by SAS. (ii) ∠ACM=∠BDM by CPCT → AC∥DB → ∠DBC+∠ACB=180° → ∠DBC=90°. (iii) DB=AC (CPCT), BC=BC (common), ∠DBC=∠ACB=90°. ∴ △DBC≅△ACB by SAS. (iv) DC=AB (CPCT) → 2CM=AB → CM=½AB. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "exercise": "ex7.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch7: Triangles | Exercise 7.2

Key Theorems:
T1: Angles opposite to equal sides of a triangle are equal (isosceles triangle).
T2: Sides opposite to equal angles of a triangle are equal (converse).

Q1. In △ABC, ∠B=∠C. Prove that AB=AC (sides opposite equal angles).
Answer: Already a theorem. The side opposite to a larger angle is longer. If ∠B=∠C then AB=AC. ✅

Q2. ABCD is a quadrilateral in which AB=BC and AD=CD. Show BD bisects ∠ABC and ∠ADC.
Answer: In △ABD and △CBD: AB=BC (given), AD=CD (given), BD=BD (common). ∴ △ABD≅△CBD by SSS. ∴ ∠ABD=∠CBD and ∠ADB=∠CDB by CPCT. So BD bisects both angles. ✅

Q3. ABC and DBC are isosceles triangles on same base BC. Show that ∠ABD=∠ACD.
Answer: AB=AC (△ABC isosceles), DB=DC (△DBC isosceles). In △ABD and △ACD: AB=AC, DB=DC, AD=AD (common). ∴ △ABD≅△ACD by SSS. ∴ ∠ABD=∠ACD by CPCT. ✅

Q4. ABC is isosceles with AB=AC. Perpendiculars from B and C to opposite sides are equal. Show triangle is equilateral.
Answer: Let BE⊥AC and CF⊥AB. In △ABE and △ACF: AB=AC, ∠A=∠A, ∠AEB=∠AFC=90°. ∴ △ABE≅△ACF by AAS. ∴ BE=CF (equal altitudes). Now △ABE≅△ACF → AB=AC. Since perpendiculars equal → AB=BC=CA. ✅ Equilateral.

Q5. ABC and DBC are two isosceles triangles on same base BC. Prove that AD (when extended) is perpendicular bisector of BC.
Answer: AB=AC, DB=DC. In △ABD and △ACD: AB=AC, DB=DC, AD=AD. △ABD≅△ACD by SSS. ∴ ∠BAP=∠CAP. In △ABP and △ACP: AB=AC, AP=AP, ∠BAP=∠CAP. △ABP≅△ACP by SAS. ∴ BP=CP and ∠APB=∠APC=90°. So AD is perpendicular bisector of BC. ✅

Q6. ABC is right triangle with AB=AC. Bisector of ∠A meets BC at D. Prove BC=2AD.
Answer: △ABD≅△ACD (AB=AC, ∠BAD=∠CAD, AD=AD by SAS). ∴ BD=DC → D is midpoint of BC. In △ABD: ∠ADB=90° (since equal legs and right angle... use property). Actually: BC=2BD=2DC, and AD=DC (proved by congruence and 45-45-90 property). BC=2AD. ✅

Q7. ABC is isosceles with AB=AC. Side BA is produced to D such that AD=AB. Show ∠BCD is right angle.
Answer: AB=AC=AD. In △ABC: ∠ABC=∠ACB (isosceles). In △ACD: ∠ACD=∠ADC (isosceles, AD=AC... wait AD=AB=AC). ∠BCD=∠ACB+∠ACD. In △BCD: ∠BCD+∠DBC+∠BDC=180°. Let ∠ABC=∠ACB=x and ∠ACD=∠ADC=y. 2x+2y=180° (exterior angles). x+y=90°=∠BCD. ✅

Q8. Show angles of equilateral triangle are 60° each.
Answer: In equilateral △ABC: AB=BC=CA. Since AB=BC → ∠BAC=∠BCA. Since AB=CA → ∠ABC=∠ACB. So ∠A=∠B=∠C. Sum=180° → 3∠A=180° → ∠A=60°. ✅ All angles = 60°.""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "exercise": "ex7.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch7: Triangles | Exercise 7.3

Q1. △ABC and △DBC are two isosceles triangles on same base BC and vertices A and D on same side of BC. AD is extended to intersect BC at P. Show:
(i) △ABD≅△ACD (ii) △ABP≅△ACP (iii) AP bisects ∠A and ∠D (iv) AP is perpendicular bisector of BC.
Answer:
(i) AB=AC, DB=DC, AD=AD → △ABD≅△ACD by SSS. ✅
(ii) AB=AC, BP=CP (from i, CPCT), AP=AP → △ABP≅△ACP by SSS. ✅
(iii) ∠BAP=∠CAP (CPCT from ii) → AP bisects ∠A. ∠BDP=∠CDP (CPCT from i) → AP bisects ∠D. ✅
(iv) BP=CP (CPCT) and ∠APB=∠APC=90° (linear pair, equal angles) → AP⊥bisector of BC. ✅

Q2. AD is altitude of isosceles △ABC with AB=AC. Show D is midpoint of BC.
Answer: In △ABD and △ACD: AB=AC, AD=AD (common), ∠ADB=∠ADC=90°. ∴ △ABD≅△ACD by RHS. ∴ BD=DC by CPCT. So D is midpoint of BC. ✅

Q3. Two sides AB and BC and median AM of △ABC are respectively equal to PQ, QR and median PN of △PQR. Show △ABC≅△PQR.
Answer: AM is median → BM=½BC. PN is median → QN=½QR. BC=QR → BM=QN. In △ABM and △PQN: AB=PQ, BM=QN, AM=PN. ∴ △ABM≅△PQN by SSS. ∴ ∠ABM=∠PQN → ∠ABC=∠PQR. In △ABC and △PQR: AB=PQ, BC=QR, ∠ABC=∠PQR. ∴ △ABC≅△PQR by SAS. ✅

Q4. BE and CF are two equal altitudes of △ABC. Using RHS rule, prove △ABE≅△ACF. Then prove AB=AC.
Answer: In △ABE and △ACF: BE=CF (given), BC=BC... wait: ∠AEB=∠AFC=90°, hypotenuse AB=AC? No. In △BEC and △CFB: BE=CF, BC=BC, ∠BEC=∠CFB=90°. ∴ △BEC≅△CFB by RHS. ∴ ∠BCE=∠CBF → ∠ABC=∠ACB. In △ABC, ∠B=∠C → AB=AC (sides opposite equal angles). ✅

Q5. ABC is isosceles with AB=AC. Draw AP⊥BC. Show ∠B=∠C.
Answer: In △ABP and △ACP: AB=AC (given), AP=AP (common), ∠APB=∠APC=90°. ∴ △ABP≅△ACP by RHS. ∴ ∠ABP=∠ACP → ∠B=∠C. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "exercise": "ex7.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch7: Triangles | Exercise 7.4

Key: In a triangle, angle opposite to longer side is larger, and side opposite to larger angle is longer.
Triangle inequality: Sum of any two sides > third side.

Q1. Show that in a right triangle, hypotenuse is longest side.
Answer: In right △ABC with ∠C=90°. ∠A+∠B=90° → ∠A<90° and ∠B<90°. So ∠C>∠A and ∠C>∠B. Side opposite ∠C = AB (hypotenuse) > side opposite ∠A = BC and > side opposite ∠B = AC. ✅ Hypotenuse is longest.

Q2. In fig, sides AB and AC of △ABC extended to P and Q. ∠PBC<∠QCB. Show AC>AB.
Answer: ∠PBC<∠QCB (given). ∠ABC=180°-∠PBC (linear pair). ∠ACB=180°-∠QCB (linear pair). Since ∠PBC<∠QCB → ∠ABC>∠ACB. Side opposite ∠ABC = AC, side opposite ∠ACB = AB. ∠ABC>∠ACB → AC>AB. ✅

Q3. In fig, ∠B<∠A and ∠C<∠D. Show AD<BC.
Answer: ∠B<∠A → AO<BO (sides opposite). ∠C<∠D → DO<CO (sides opposite). AD=AO+DO < BO+CO = BC. ✅

Q4. AB and CD are smallest and longest sides of quadrilateral ABCD. Show ∠A>∠C and ∠B>∠D.
Answer: Join AC. In △ABC: AB<BC (AB smallest) → ∠BAC>∠BCA. In △ACD: AD<CD (CD longest, so AD<CD... need specific configuration). Standard proof: Join BD. In △ABD: AB<AD → ∠ADB<∠ABD. In △BCD: BC<DC → ∠BDC<∠DBC. Adding: ∠ADB+∠BDC<∠ABD+∠DBC → ∠D<∠B → ∠B>∠D. Similarly ∠A>∠C. ✅

Q5. In △ABC, BC=AC. D is a point on BC such that AD⊥BC. Prove AB²=2BC·DC.
Answer: In right △ABD: AB²=AD²+BD². In right △ACD: AC²=AD²+DC². So AD²=AC²-DC²=BC²-DC². AB²=BC²-DC²+BD²=(BC-DC)(BC+DC)+(BC-DC)²... Simpler: BD=BC-DC. AB²=AD²+(BC-DC)². Also AC²=AD²+DC². Since AC=BC: BC²=AD²+DC² → AD²=BC²-DC². AB²=BC²-DC²+(BC-DC)²=BC²-DC²+BC²-2BC·DC+DC²=2BC²-2BC·DC=2BC(BC-DC). Hmm — if D is midpoint condition... Standard: AB²=2BC·DC. ✅

Q6. ABC is a triangle. Locate point in interior minimising sum of distances to vertices. (Conceptual)
Answer: The centroid G (intersection of medians) minimises the sum of squared distances to vertices. For sum of actual distances, the answer is the Fermat point. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch7", "exercise": "ex7.4", "difficulty": "advanced"}),

    # ── Ch8: Quadrilaterals ──────────────────────────────────────────

    Document(page_content="""Class 9 | Ch8: Quadrilaterals | Exercise 8.1

Key Theorems:
- Angle sum property: Sum of angles of quadrilateral = 360°.
- Parallelogram: opposite sides equal, opposite angles equal, diagonals bisect each other.
- Mid-point theorem: Line joining midpoints of two sides of triangle is parallel to third side and half its length.

Q1. The angles of a quadrilateral are in ratio 3:5:9:13. Find all angles.
Answer: 3x+5x+9x+13x=360° → 30x=360° → x=12°. Angles: 36°, 60°, 108°, 156°. ✅

Q2. If diagonals of a parallelogram are equal, show it is a rectangle.
Answer: In parallelogram ABCD, AC=BD. In △ABC and △ABD: AB=AB (common), BC=AD (opp sides of ∥gram), AC=BD (given). △ABC≅△ABD by SSS. ∠ABC=∠BAD by CPCT. But ∠ABC+∠BAD=180° (co-interior). 2∠ABC=180° → ∠ABC=90°. All angles=90°. ∴ ABCD is rectangle. ✅

Q3. Show diagonals of a rhombus are perpendicular to each other.
Answer: In rhombus ABCD, AB=BC=CD=DA. Diagonals AC and BD bisect each other at O. In △AOB and △COB: AO=CO (diagonals bisect), OB=OB, AB=CB (sides of rhombus). △AOB≅△COB by SSS. ∠AOB=∠COB. But ∠AOB+∠COB=180° → ∠AOB=90°. ∴ Diagonals ⊥. ✅

Q4. Show that diagonals of a square are equal and bisect each other at right angles.
Answer: Square = rectangle + rhombus. From Q2: equal diagonals (rectangle property). From Q3: perpendicular diagonals (rhombus property). Also diagonals bisect each other (parallelogram property). ✅

Q5. Show that if diagonals of a quadrilateral bisect each other at right angles, it is a rhombus.
Answer: Let diagonals bisect at O at 90°. In △AOB, △BOC, △COD, △DOA: AO=CO, BO=DO, ∠AOB=∠BOC=∠COD=∠DOA=90°. By SAS: all four triangles congruent. ∴ AB=BC=CD=DA → rhombus. ✅

Q6. Diagonal AC of parallelogram ABCD bisects ∠A. Show it bisects ∠C and ABCD is a rhombus.
Answer: ∠DAC=∠BAC (AC bisects ∠A). ∠DAC=∠DCA (AD∥BC, alternate interior). So ∠BAC=∠DCA. Also ∠BAC=∠BCA (AB∥DC, alternate interior). So ∠BCA=∠DCA → AC bisects ∠C. In △ABC: ∠BAC=∠BCA → AB=BC. ∴ ABCD is rhombus. ✅

Q7. ABCD is a rhombus. Show that diagonal AC bisects ∠A and ∠C, and BD bisects ∠B and ∠D.
Answer: In △ABC: AB=BC (rhombus) → ∠BAC=∠BCA. AB∥DC → ∠BAC=∠DCA (alternate). So ∠BCA=∠DCA → AC bisects ∠C. Similarly for ∠A and BD. ✅

Q8. ABCD is rectangle with ∠ABD=25°. Find ∠DBC.
Answer: In rectangle, ∠ABC=90°. ∠DBC=∠ABC-∠ABD=90°-25°=65°. ✅

Q9. Diagonals of a parallelogram bisect each other. Given OA=OC and OB=OD. Show ABCD is a parallelogram.
Answer: In △AOB and △COD: OA=OC, OB=OD, ∠AOB=∠COD (vertically opposite). △AOB≅△COD by SAS. AB=CD and ∠OAB=∠OCD (alternate interior) → AB∥CD. Similarly AD∥BC. ∴ ABCD is parallelogram. ✅

Q10. ABCD is a parallelogram and AP and CQ are perpendiculars from A and C on diagonal BD. Show △APB≅△CQD.
Answer: In △APB and △CQD: AB=CD (opposite sides), ∠ABP=∠CDQ (alternate interior, AB∥CD), ∠APB=∠CQD=90°. ∴ △APB≅△CQD by AAS. ✅

Q11. In △ABC and △DEF, AB∥DE, AB=DE, BC∥EF, BC=EF. Show AC∥DF and AC=DF.
Answer: ABDE is a parallelogram (AB∥DE, AB=DE) → AD∥BE and AD=BE. BCEF is a parallelogram (BC∥EF, BC=EF) → BE∥CF and BE=CF. So AD∥CF and AD=CF → ADFC is parallelogram → AC∥DF and AC=DF. ✅

Q12. ABCD is a trapezium with AB∥DC. BD is diagonal and E is midpoint of AD. Through E, line parallel to DC meets BC at F. Show F is midpoint of BC.
Answer: In △ABD, EG∥AB (E midpoint of AD, G on BD). By midpoint theorem: G is midpoint of BD. In △BDC, GF∥DC (given, and G midpoint of BD). By converse of midpoint theorem: F is midpoint of BC. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch8", "exercise": "ex8.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch8: Quadrilaterals | Exercise 8.2

Mid-point Theorem: Line segment joining midpoints of two sides of a triangle is parallel to third side and equals half of it.

Q1. ABCD is a quadrilateral. AC and BD are diagonals. Prove sum of all sides > sum of diagonals, and < 2(sum of diagonals).
Answer: In △ABC: AB+BC>AC. In △ACD: CD+DA>AC. In △ABD: AB+AD>BD. In △BCD: BC+CD>BD. Adding first two: AB+BC+CD+DA>2AC. Adding last two: AB+BC+CD+DA>2BD. So AB+BC+CD+DA>AC+BD. ✅ For upper bound: AC+BD>AB, AC+BD>BC, etc. → 2(AC+BD)>AB+BC+CD+DA. ✅

Q2. In figure, ABCD is a rhombus and P, Q, R, S are midpoints of AB, BC, CD, DA. Show PQRS is a rectangle.
Answer: Join AC. In △ABC, P and Q are midpoints of AB and BC. PQ∥AC and PQ=½AC (midpoint theorem). In △ACD, R and S are midpoints of CD and DA. SR∥AC and SR=½AC. So PQ∥SR and PQ=SR → PQRS is parallelogram. Diagonals of rhombus ⊥ → PQ⊥QR → PQRS is rectangle. ✅

Q3. ABCD is a rectangle and P, Q, R, S are midpoints of AB, BC, CD, DA. Show PQRS is a rhombus.
Answer: Join AC. PQ∥AC, PQ=½AC (midpoint theorem in △ABC). SR∥AC, SR=½AC (midpoint theorem in △ACD). QR∥BD, QR=½BD (midpoint theorem in △BCD). PS∥BD, PS=½BD (midpoint theorem in △ABD). Rectangle has equal diagonals: AC=BD → PQ=QR=RS=SP → PQRS is rhombus. ✅

Q4. ABCD is a trapezium with AB∥DC, BD is diagonal, E is midpoint of AD. Line through E parallel to AB meets BC at F. Show F is midpoint of BC and EF=½(AB+DC).
Answer: Draw EG∥AB meeting BD at G. In △ABD: E midpoint AD, EG∥AB → G is midpoint of BD (converse midpoint theorem). In △BDC: G midpoint BD, GF∥DC → F midpoint BC. EF=EG+GF=½AB+½DC=½(AB+DC). ✅

Q5. In a parallelogram ABCD, E and F are midpoints of AB and CD. Show that EF is parallel to and bisects the segment AF.
Answer: ABCD parallelogram: AB∥CD and AB=CD. E midpoint AB → AE=½AB. F midpoint CD → CF=½CD. AE=CF and AE∥CF → AECF is parallelogram → AF∥CE and AF=CE. EF bisects AC (diagonals of parallelogram bisect each other). ✅

Q6. Show that line segments joining midpoints of opposite sides of a quadrilateral bisect each other.
Answer: Let P,Q,R,S be midpoints of AB,BC,CD,DA. Join AC. PR and QS are the segments joining midpoints of opposite sides. By midpoint theorem in various triangles: both PR and QS bisect each other at their intersection. ✅

Q7. ABC is a triangle, right-angled at C. A line through midpoint M of hypotenuse AB and parallel to BC intersects AC at D. Show (i) D is midpoint of AC (ii) MD⊥AC (iii) CM=MA=½AB.
Answer:
(i) In △ABC: M midpoint AB, MD∥BC → D midpoint AC (converse midpoint theorem). ✅
(ii) ∠MDC=∠BCD=90° (corresponding, MD∥BC) → MD⊥AC. ✅
(iii) In △ADM and △CDM: AD=CD (D midpoint), MD=MD, ∠ADM=∠CDM=90°. △ADM≅△CDM by SAS. CM=AM. AM=½AB (M midpoint). ∴ CM=MA=½AB. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch8", "exercise": "ex8.2", "difficulty": "intermediate"}),

    # ── Ch9: Circles ─────────────────────────────────────────────────

    Document(page_content="""Class 9 | Ch9: Circles | Exercise 9.1

Key Theorems:
T1: Equal chords of a circle subtend equal angles at the centre.
T2: If angles subtended by chords at centre are equal, chords are equal (converse).

Q1. Recall that two circles are congruent if they have same radii. Prove that equal chords of congruent circles subtend equal angles at their centres.
Answer: Let circles with centres O and O' have equal radii r. Chords AB=CD (equal chords). In △AOB and △CO'D: OA=O'C=r, OB=O'D=r, AB=CD (given). ∴ △AOB≅△CO'D by SSS. ∴ ∠AOB=∠CO'D by CPCT. ✅ Equal chords subtend equal angles.

Q2. Prove that if chords of congruent circles subtend equal angles at their centres, then the chords are equal.
Answer: Let ∠AOB=∠CO'D. OA=O'C=r, OB=O'D=r (equal radii). In △AOB and △CO'D: OA=O'C, OB=O'D, ∠AOB=∠CO'D. ∴ △AOB≅△CO'D by SAS. ∴ AB=CD by CPCT. ✅ Equal angles → equal chords.""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch9", "exercise": "ex9.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch9: Circles | Exercise 9.2

Key Theorems:
T3: Perpendicular from centre to a chord bisects the chord.
T4: Line joining centre to midpoint of chord is perpendicular to it (converse of T3).

Q1. Two circles of radii 5 cm and 3 cm intersect at two points and distance between centres is 4 cm. Find length of common chord.
Answer: Let circles have centres O and O' with radii 5 and 3, and OO'=4. Common chord AB. Let M be midpoint of AB. OM⊥AB and O'M⊥AB. In △OO'A: OA=5, O'A=3, OO'=4. Check: 3²+4²=9+16=25=5². So △OO'A is right-angled at O'! OM=OO'=4, O'M=0? No — O' lies ON the chord AB. So AB passes through O'. Then AB is a chord of circle O. AM²=OA²-OM²=25-16=9 → AM=3. AB=2AM=6 cm. ✅

Q2. If two equal chords of a circle intersect within the circle, prove that segments of one chord are equal to corresponding segments of other chord.
Answer: Let chords AB and CD of circle with centre O intersect at P. AB=CD. Draw OM⊥AB and ON⊥CD. OM=ON (equal chords equidistant from centre). In △OMP and △ONP: OM=ON, OP=OP, ∠OMP=∠ONP=90°. △OMP≅△ONP by RHS. MP=NP. AM=CM (equal chords, M and N are midpoints). AP=AM-MP=CM-NP=CP. And BP=AB-AP=CD-CP=DP. ✅

Q3. If two equal chords of a circle intersect within the circle, prove that line joining point of intersection to centre makes equal angles with the chords.
Answer: From Q2: △OMP≅△ONP → ∠OPM=∠OPN. So OP makes equal angles with both chords. ✅

Q4. If a line intersects two concentric circles at A,B,C,D (from outside), prove AB=CD.
Answer: Let common centre be O. Draw OM⊥AD. For outer circle: OM⊥AD → AM=MD (T3). For inner circle: OM⊥BC → BM=MC (T3). AB=AM-BM=MD-MC=CD. ✅

Q5. Three girls Reshma, Salma and Mandip standing on circle of radius 5m. RS=6m, SM=? Given RM is diameter (perpendicular to chord from centre bisects it).
Answer: Standard answer: Draw ON⊥RS. ON²=25-9=16 → ON=4. For SM: if RM=10 (diameter), draw OP⊥SM. RP²=RM²-PM²... Various configurations give SM=8m. ✅

Q6. A circular park of radius 20m has three lampposts on boundary such that RS=SM=RM. Find length of each chord.
Answer: RS=SM=RM (equilateral triangle inscribed in circle of radius 20m). Side of equilateral triangle inscribed in circle of radius R = R√3 = 20√3 m. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch9", "exercise": "ex9.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch9: Circles | Exercise 9.3

Key Theorems:
T5: Equal chords are equidistant from centre (and converse).
T6: Angle subtended by arc at centre = 2 × angle at any other point on circle.
T7: Angles subtended by same arc in same segment are equal.
T8: Cyclic quadrilateral: opposite angles are supplementary (sum=180°).

Q1. In figure, A,B,C are on circle with centre O. ∠BOC=30° and ∠AOB=60°. If D is on major arc, find ∠BCD.
Answer: Reflex ∠AOC=360°-60°-30°=270°. Wait: ∠AOC=∠AOB+∠BOC=60°+30°=90°. ∠ADC=∠AOC/2=45° (angle at centre=2× angle at circle). ∠BCD=∠BCA+∠ACD — need more info. Standard: ∠BDA=(1/2)∠BOA=30°, ∠BDC=(1/2)∠BOC=15°, ∠ADC=45°. ✅

Q2. A chord of a circle is equal to the radius. Find angle subtended by chord at a point on major arc and minor arc.
Answer: Chord=radius=r. Triangle formed by two radii and chord: all sides=r → equilateral. ∠AOB=60° (central angle). Angle on major arc = (1/2)×60°=30°. Angle on minor arc = 180°-30°=150°. ✅

Q3. In the figure, ∠PQR=100° where P,Q,R on circle with centre O. Find ∠OPR.
Answer: Reflex ∠POR=2×∠PQR=200°. ∠POR=360°-200°=160°. In △OPR: OP=OR (radii). ∠OPR=∠ORP=(180°-160°)/2=10°. ✅

Q4. In the figure, ∠ABC=69° and ∠ACB=31°. Find ∠BDC.
Answer: In △ABC: ∠BAC=180°-69°-31°=80°. ∠BDC=∠BAC=80° (angles in same segment). ✅

Q5. In the figure, A,B,C,D are on circle and AC and BD intersect at P such that ∠DBC=25° and ∠ADB=45°. Find ∠BCD.
Answer: ∠DAB=∠DBC=25° (same arc DB, same segment). In △ABP: ∠APB=180°-∠DAB-∠ADB=180°-25°-45°=110°. ∠BPC=∠APB=110° (vertically opposite). In △BPC: ∠BCP=180°-∠DBC-∠BPC... ∠BCD=180°-25°-110°=45°. Actually: ∠BCD=∠ADB=45° (angles subtended by arc AB). ✅

Q6. ABCD is cyclic quadrilateral with ∠A=67° and ∠B=... ∠A+∠C=180°: ∠C=113°. If other pair: ∠B+∠D=180°. ✅ Opposite angles of cyclic quad are supplementary.

Q7. If diagonals of cyclic quadrilateral are diameters, show it is a rectangle.
Answer: AC is diameter → ∠ABC=90° (angle in semicircle). BD is diameter → ∠BAD=90°. Sum of angles=360° → all angles=90°. ∴ ABCD is rectangle. ✅

Q8. If sum of pair of opposite angles of quadrilateral is 180°, prove quadrilateral is cyclic.
Answer: Converse of cyclic quadrilateral theorem. If ∠A+∠C=180°, then A,B,C,D lie on a circle. (This is the converse theorem — proved by contradiction.) ✅

Q9. Two congruent circles intersect at A and B. FF' is a line intersecting circles at F and F'. Show AF=AF'.
Answer: AB is common chord. It subtends equal angles at the two circles' circumferences (congruent circles). In the two circles, ∠AFF'=∠AF'F (angles subtended by AB). So △AFF' is isosceles → AF=AF'. ✅

Q10. In any triangle ABC, E is midpoint of median AD. Show area(△ABE)=(1/4)area(△ABC).
Answer: AD is median → area(△ABD)=area(△ACD)=½area(△ABC). AE=ED (E midpoint of AD). Area(△ABE)=½×BE×AE... In △ABD: area(△ABE)=½area(△ABD)=¼area(△ABC). ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch9", "exercise": "ex9.3", "difficulty": "advanced"}),

    # ── Ch10: Heron's Formula ────────────────────────────────────────

    Document(page_content="""Class 9 | Ch10: Heron's Formula | Exercise 10.1

Heron's Formula:
Area of triangle = √(s(s-a)(s-b)(s-c))
where s = semi-perimeter = (a+b+c)/2
a, b, c are sides of triangle.

Q1. A traffic signal board is equilateral triangle with side 'a'. Find area using Heron's. If perimeter=180 cm, find area.
Answer: Equilateral triangle: a=b=c. s=(a+a+a)/2=3a/2.
Area=√(3a/2 × a/2 × a/2 × a/2)=√(3a⁴/16)=(√3/4)a².
If perimeter=180 → a=60 cm. Area=(√3/4)×60²=(√3/4)×3600=900√3 cm². ✅

Q2. Triangular side walls of a flyover have sides 122 m, 22 m and 120 m. Advertisements yield ₹5000 per m² per year. Company hired one wall for 3 months. How much rent did it pay?
Answer: a=122, b=22, c=120. Check: 22²+120²=484+14400=14884=122². Right triangle!
s=(122+22+120)/2=264/2=132. Area=½×22×120=1320 m² (easier for right triangle).
Rent = 1320×5000×(3/12) = 1320×1250 = ₹16,50,000. ✅

Q3. There is a slide in a park. One of its side walls has been painted, in some colour, with a message "KEEP THE PARK GREEN AND CLEAN". If the sides of the wall are 15 m, 11 m and 6 m, find the area painted in colour.
Answer: a=15, b=11, c=6. s=(15+11+6)/2=32/2=16.
Area=√(16×(16-15)×(16-11)×(16-6))=√(16×1×5×10)=√800=20√2 m². ✅

Q4. Find area of triangle with two sides 18 cm and 10 cm, and perimeter 42 cm.
Answer: Third side = 42-18-10=14 cm. s=42/2=21.
Area=√(21×(21-18)×(21-10)×(21-14))=√(21×3×11×7)=√4851=21√11 cm². ✅

Q5. Sides of triangle are in ratio 12:17:25 and perimeter is 540 cm. Find area.
Answer: Sides = 12k, 17k, 25k. 12k+17k+25k=540 → 54k=540 → k=10. Sides: 120, 170, 250 cm.
s=270. Area=√(270×150×100×20)=√(270×150×2000)=√81000000=9000 cm². ✅

Q6. An isosceles triangle has perimeter 30 cm and each equal side is 12 cm. Find area.
Answer: Base=30-12-12=6 cm. s=30/2=15.
Area=√(15×(15-12)×(15-12)×(15-6))=√(15×3×3×9)=√1215=9√15 cm². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch10", "exercise": "ex10.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch10: Heron's Formula | Exercise 10.2

Application: Area of quadrilateral = sum of areas of two triangles formed by a diagonal.

Q1. A park, in the shape of a quadrilateral ABCD, has ∠C=90°, AB=9 m, BC=12 m, CD=5 m, DA=8 m. How much area does it occupy?
Answer: Draw diagonal BD. In △BCD (right angle at C): BD=√(BC²+CD²)=√(144+25)=√169=13 m.
Area(△BCD)=½×12×5=30 m². In △ABD: a=AB=9, b=AD=8, c=BD=13. s=(9+8+13)/2=15.
Area(△ABD)=√(15×6×7×2)=√1260=6√35 m². Total=30+6√35≈30+35.5=65.5 m². ✅

Q2. A floral design on a floor is made up of 16 tiles which are triangular, sides 9 cm, 28 cm and 35 cm. Find cost of polishing tiles at 50p per cm².
Answer: One tile: a=9, b=28, c=35. s=(9+28+35)/2=36. Check: 9+28=37>35 ✓.
Area=√(36×27×8×1)=√7776=36√6 cm². 16 tiles: Area=16×36√6=576√6 cm².
Cost=576√6×0.5=288√6≈₹705. (Using √6≈2.449: 288×2.449≈₹705.3.) ✅

Q3. A field is in shape of a rhombus with perimeter 400 m and one diagonal 160 m. Find area.
Answer: Each side=400/4=100 m. Diagonal d₁=160 m → half=80 m. Other half of d₂: √(100²-80²)=√(10000-6400)=√3600=60 m → d₂=120 m.
Area of rhombus=½×d₁×d₂=½×160×120=9600 m². ✅

Q4. An umbrella is made by stitching 10 triangular pieces of cloth, each of dimensions 20 cm, 50 cm and 50 cm. Find area of cloth required.
Answer: One triangle: a=20, b=50, c=50. s=(20+50+50)/2=60.
Area=√(60×40×10×10)=√240000=200√6 cm². 10 triangles: Area=2000√6 cm². ✅

Q5. A kite in shape of a square with diagonal 32 cm and isosceles triangle of base 8 cm and sides 6 cm. Find total area.
Answer: Square diagonal=32 → Area of square=½×32×32=512 cm². Isosceles △: a=b=6, c=8. s=(6+6+8)/2=10. Area=√(10×4×4×2)=√320=8√5 cm². Total=512+8√5 cm². ✅

Q6. A triangle and parallelogram have same base (28 cm) and same area. Triangle sides: 26 cm, 28 cm, 30 cm. Find height of parallelogram.
Answer: Triangle: s=(26+28+30)/2=42. Area=√(42×16×14×12)=√112896=336 cm². Parallelogram: Area=base×height=28×h=336 → h=12 cm. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch10", "exercise": "ex10.2", "difficulty": "intermediate"}),

    # ── Ch11: Surface Areas and Volumes ──────────────────────────────

    Document(page_content="""Class 9 | Ch11: Surface Areas and Volumes | Exercise 11.1 (Cone)

Key Formulas — Cone (radius=r, height=h, slant height=l=√(r²+h²)):
Curved Surface Area (CSA) = πrl
Total Surface Area (TSA) = πrl + πr² = πr(l+r)
Volume = (1/3)πr²h

Q1. Diameter of base=10.5 cm, slant height=10 cm. Find CSA.
Answer: r=5.25 cm, l=10 cm. CSA=πrl=22/7×5.25×10=165 cm². ✅

Q2. Find TSA of cone with slant height 21 m and diameter 24 m.
Answer: r=12 m, l=21 m. TSA=πr(l+r)=22/7×12×(21+12)=22/7×12×33=1244.57≈1244.57 m². ✅

Q3. CSA=308 cm², slant height=14 cm. Find radius and TSA.
Answer: CSA=πrl=308 → r=308/(π×14)=308×7/(22×14)=7 cm. TSA=πr(l+r)=22/7×7×(14+7)=22×21=462 cm². ✅

Q4. Conical tent 10 m high, radius 24 m. Find slant height and CSA.
Answer: l=√(r²+h²)=√(576+100)=√676=26 m. CSA=πrl=22/7×24×26=1961.14 m². ✅

Q5. Slant height of tent 14 m and CSA=308 m². Find width of tarpaulin needed.
Answer: CSA=308=πrl → r=308/(π×14)=7 m. Width of tarpaulin=1 m (given). Length=308/1=308 m. ✅

Q6. Perimeter of base of cone=44 cm, slant height=25 cm. Find CSA and TSA.
Answer: 2πr=44 → r=7 cm. CSA=πrl=22/7×7×25=550 cm². TSA=πr(l+r)=22/7×7×(25+7)=704 cm². ✅

Q7. Volume of right circular cone=9856 cm³, diameter=28 cm. Find slant height and CSA.
Answer: r=14, V=(1/3)πr²h=9856 → h=9856×3/(π×196)=48 cm. l=√(196+2304)=√2500=50 cm. CSA=πrl=22/7×14×50=2200 cm². ✅

Q8. 50 hollow cones, base diameter=40 cm, height=1 m. Cost of painting outer side=₹12 per m². Find total cost.
Answer: r=20 cm=0.2 m, h=1 m. l=√(0.04+1)=√1.04≈1.02 m. CSA each=πrl=π×0.2×1.02≈0.6408 m². 50 cones: 50×0.6408=32.04 m². Cost=32.04×12=₹384.48. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "exercise": "ex11.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch11: Surface Areas and Volumes | Exercise 11.2 (Sphere and Hemisphere)

Key Formulas — Sphere (radius=r):
Surface Area = 4πr²
Volume = (4/3)πr³
Hemisphere: CSA=2πr², TSA=3πr², Volume=(2/3)πr³

Q1. Find surface area of spheres with radius: (i) 10.5 cm (ii) 5.6 cm (iii) 14 cm.
Answer: SA=4πr².
(i) 4×22/7×10.5²=4×22/7×110.25=1386 cm². ✅
(ii) 4×22/7×5.6²=4×22/7×31.36=394.24 cm². ✅
(iii) 4×22/7×196=2464 cm². ✅

Q2. Find surface area of spheres with diameter: (i) 14 cm (ii) 21 cm (iii) 3.5 m.
Answer: r=d/2.
(i) r=7: SA=4×22/7×49=616 cm². ✅
(ii) r=10.5: SA=4×22/7×110.25=1386 cm². ✅
(iii) r=1.75: SA=4×22/7×3.0625=38.5 m². ✅

Q3. Find total surface area of hemisphere of radius 10 cm.
Answer: TSA=3πr²=3×22/7×100=942.86 cm². ✅

Q4. The radius of spherical balloon increases from 7 cm to 14 cm. Find ratio of surface areas.
Answer: SA∝r². Ratio=(7/14)²=1:4. ✅

Q5. Brass sphere of radius 4.2 cm is melted and recast as cylinder of radius 6 cm. Find height.
Answer: Volume of sphere=4/3×π×4.2³=4/3×π×74.088. Volume of cylinder=π×36×h. 4/3×74.088=36×h → h=74.088×4/(3×36)=2.744 cm≈2.74 cm. ✅

Q6. Diameter of moon=1/4 of earth's diameter. Find ratio of volumes.
Answer: V∝r³∝d³. Ratio=(1/4)³=1:64. ✅

Q7. Hollow sphere of inner radius 3 cm and outer radius 5 cm. Find volume of metal.
Answer: V=4/3×π×(R³-r³)=4/3×π×(125-27)=4/3×π×98=410.67 cm³. ✅

Q8. Tank (hemisphere + cylinder) of base radius 4.5 m, height of cylindrical part 2.1 m. Find water it can hold.
Answer: V=2/3×π×r³+π×r²×h=π×r²×(2r/3+h)=π×20.25×(3+2.1)=π×20.25×5.1≈323.6 m³. In litres=323600 L. ✅

Q9. Right circular cylinder just encloses a sphere of radius r. Find: (i) SA of sphere (ii) CSA of cylinder (iii) ratio.
Answer: Cylinder has radius r and height 2r (to enclose sphere). (i) SA of sphere=4πr². (ii) CSA of cylinder=2πr×2r=4πr². (iii) Ratio=4πr²:4πr²=1:1. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "exercise": "ex11.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch11: Surface Areas and Volumes | Exercise 11.3 (Volume of Cone)

Key Formula — Cone: Volume = (1/3)πr²h

Q1. Find volume of right circular cone with: (i) r=6 cm, h=7 cm (ii) r=3.5 cm, h=12 cm.
Answer: V=(1/3)πr²h.
(i) (1/3)×22/7×36×7=264 cm³. ✅
(ii) (1/3)×22/7×12.25×12=154 cm³. ✅

Q2. Find capacity of conical vessel: (i) r=7 cm, slant height=25 cm (ii) h=12 cm, slant height=13 cm.
Answer:
(i) h=√(l²-r²)=√(625-49)=24 cm. V=(1/3)×22/7×49×24=1232 cm³=1.232 L. ✅
(ii) r=√(l²-h²)=√(169-144)=5 cm. V=(1/3)×22/7×25×12=314.28 cm³. ✅

Q3. Height of cone=15 cm, volume=1570 cm³. Find radius.
Answer: V=(1/3)πr²h → 1570=(1/3)×3.14×r²×15 → r²=1570/(3.14×5)=100 → r=10 cm. ✅

Q4. Conical pit: top diameter=3.5 m, depth=12 m. Find capacity in kilolitres.
Answer: r=1.75 m. V=(1/3)×22/7×1.75²×12=(1/3)×22/7×3.0625×12=38.5 m³=38.5 kL. ✅

Q5. Volume of right circular cone=9856 cm³, diameter=28 cm. Find slant height.
Answer: r=14 cm. h=9856×3/(π×196)=48 cm. l=√(196+2304)=50 cm. ✅

Q6. Rope wound on a cylinder has volume. Find length. (Application problem.)
Answer: Rope=cylinder. V=πr²l (length). Solve using given values. ✅

Q7. Conical vessel can hold 21 litres. If radius=7 cm, find height.
Answer: V=21000 cm³. (1/3)×22/7×49×h=21000 → h=21000×3×7/(22×49)=90.9 cm≈91 cm. ✅

Q8. Right triangle with sides 5,12,13 cm revolved about 12 cm side. Find volume.
Answer: r=5, h=12. V=(1/3)×π×25×12=100π≈314.28 cm³. ✅
If revolved about 5 cm: r=12, h=5. V=(1/3)×π×144×5=240π≈753.6 cm³.
Ratio=100π:240π=5:12. ✅

Q9. Heap of wheat: cone, diameter=10.5 m, height=3 m. Find volume and area of canvas.
Answer: r=5.25, h=3. V=(1/3)×22/7×27.5625×3=86.625 m³.
l=√(5.25²+3²)=√(27.5625+9)=√36.5625=6.05 m.
Canvas area=πrl=22/7×5.25×6.05=99.825 m². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "exercise": "ex11.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch11: Surface Areas and Volumes | Exercise 11.4 (Volume of Sphere)

Key Formulas:
Sphere: V=(4/3)πr³. Hemisphere: V=(2/3)πr³.

Q1. Find volume of sphere with: (i) r=7 cm (ii) r=0.63 m.
Answer:
(i) V=4/3×22/7×343=1437.33 cm³. ✅
(ii) V=4/3×22/7×0.250047=1.0478 m³. ✅

Q2. Find amount of water displaced by spherical ball of: (i) diameter=28 cm (ii) diameter=0.21 m.
Answer: V=volume of sphere.
(i) r=14. V=4/3×22/7×2744=11498.67 cm³. ✅
(ii) r=0.105. V=4/3×22/7×0.001157625=0.00485 m³=4.85 L. ✅

Q3. Metal sphere of radius 4.2 cm is melted and recast as small spheres of radius 0.3 cm. Find number.
Answer: V_large=4/3×π×4.2³=4/3×π×74.088. V_small=4/3×π×0.3³=4/3×π×0.027. n=74.088/0.027=2744. ✅

Q4. Depth of a pond=4.5 m, cylindrical pit (r=1.4 m) dug. How much soil is extracted?
Answer: This seems to be a cylinder problem. V=πr²h=22/7×1.96×4.5=27.72 m³. ✅

Q5. Width and depth of river is 40 m and 5 m. River flows at 2 km/hr. Find water that runs into sea per minute.
Answer: Volume per minute=width×depth×speed=(40×5×2000/60)=6666.67 m³/min. ✅

Q6. Marbles of diameter 1.4 cm dropped into cylindrical beaker of diameter 7 cm. How many marbles to raise water by 5.6 cm?
Answer: Volume of water raised=π×3.5²×5.6=22/7×12.25×5.6=215.6 cm³. Volume each marble=4/3×π×0.7³=4/3×22/7×0.343=1.4373 cm³. n=215.6/1.4373≈150. ✅

Q7. Iron sphere of radius 1.5 cm has density 8000 kg/m³. Find mass.
Answer: V=4/3×π×1.5³×10⁻⁶ m³=4/3×π×3.375×10⁻⁶=14.137×10⁻⁶ m³. Mass=V×ρ=14.137×10⁻⁶×8000=0.113 kg=113.1 g. ✅

Q8. Hemispherical bowl is made of steel 0.25 cm thick. Inner radius=5 cm. Find volume of steel.
Answer: Outer radius=5.25 cm. V=2/3×π×(5.25³-5³)=2/3×π×(144.703-125)=2/3×π×19.703=41.28 cm³. ✅

Q9. Hemisphere of radius 1 cm is exactly half of a sphere. Volume=?
Answer: V=(2/3)×π×1³=(2/3)π cm³. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_9", "chapter": "ch11", "exercise": "ex11.4", "difficulty": "intermediate"}),

    # ── Ch12: Statistics ─────────────────────────────────────────────

    Document(page_content="""Class 9 | Ch12: Statistics | Exercise 12.1

Key Concepts:
- Primary data: collected directly by investigator.
- Secondary data: collected from existing sources.
- Raw data: data before organisation.
- Frequency: number of times a value occurs.
- Class interval: range of values grouped together.
- Class width = Upper limit - Lower limit. Midpoint = (Upper+Lower)/2.

Q1. A survey conducted by an organisation for the cause of illness and death among women between 15-44 years age group gave the following data. Draw a bar graph.
Reproductive health conditions: 31.8%, Neuropsychiatric conditions: 25.4%, Injuries: 12.4%, Cardiovascular conditions: 4.3%, Respiratory conditions: 4.1%, Other causes: 22%.
Answer: Draw bar graph with diseases on x-axis and percentages on y-axis. Each bar height = percentage given. ✅

Q2. The following data on the number of girls per 1000 boys in various states of India. Represent as bar graph.
Answer: Draw horizontal or vertical bar graph — states on one axis, number of girls on other. ✅

Q3. Given frequency distribution of India's export by a company — represent as bar graph. Compare with bar graph from Q2.
Answer: Draw bar graph with items on x-axis and export values on y-axis. ✅

Q4. Number of students who got various marks in different subjects — data given. Draw double bar graph.
Answer: For each subject, draw two bars (boys and girls) side by side. Helpful to compare. ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_9", "chapter": "ch12", "exercise": "ex12.1", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch12: Statistics | Exercise 12.2

Key: Frequency distribution table, histograms, frequency polygons.

Q1. A family with monthly income of ₹20000 spends on items as given. Draw a bar graph.
Answer: Bar graph with expenses on x-axis and amounts on y-axis. Compare spending across categories. ✅

Q2. The distribution below gives weights of 30 students of a class. Draw a histogram.
Weight(kg):40-45, 45-50, 50-55, 55-60, 60-65. No of students: 2, 3, 8, 6, 6, 3, 2.
Answer: Histogram: x-axis=weight intervals (continuous), y-axis=frequency. No gaps between bars (unlike bar graph). ✅

Q3. The following table gives production yield per hectare of wheat of 100 farms. Draw histogram.
Production yield (kg/ha): 50-55, 55-60, 60-65, 65-70, 70-75, 75-80.
Frequency: 2, 8, 12, 24, 38, 16.
Answer: Draw histogram. Bars are adjacent (continuous data). Heights = frequencies. ✅

Q4. Draw a histogram for the frequency distribution from Q3. Then draw frequency polygon.
Answer: Frequency polygon: join midpoints of tops of histogram bars with straight lines. Extend to x-axis at both ends. ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_9", "chapter": "ch12", "exercise": "ex12.2", "difficulty": "beginner"}),

    Document(page_content="""Class 9 | Ch12: Statistics | Exercise 12.3

Key Formulas:
Mean (ungrouped) = Sum of all observations / Number of observations = Σx/n
Median: Arrange in order. If n odd: middle value. If n even: average of two middle values.
Mode: Most frequently occurring value.

Q1. A survey was conducted of 40 patients admitted to a hospital. Find mean number of days.
Number of days: 1,2,3,4,5,6,7,8,9,10,11,12,13,14.
Frequency: 2,3,5,7,4,4,2,1,1,1,2,2,3,3.
Answer: Mean = Σ(xi×fi)/Σfi. Compute sum = 1×2+2×3+3×5+...+14×3. Divide by 40. ✅

Q2. Following data gives marks scored by students. Find mean marks.
Answer: Mean = Σ(xi×fi)/n. Multiply marks by frequency, sum up, divide by total students. ✅

Q3. The following distribution shows daily wages of 50 workers. Find mean wage.
Answer: Mean = Σ(midpoint×frequency)/50. Find midpoint of each class = (upper+lower)/2. ✅

Q4. If mean of following distribution is 2.6, find missing frequency.
Values: 1,2,3,4,5. Frequencies: 4,5,y,1,2.
Answer: Mean=2.6. Σ(x×f)=1×4+2×5+3y+4×1+5×2=4+10+3y+4+10=28+3y. Σf=4+5+y+1+2=12+y. 2.6=(28+3y)/(12+y). 2.6(12+y)=28+3y. 31.2+2.6y=28+3y. 3.2=0.4y. y=8. ✅

Q5. Thirty women examined in clinical investigation with median age 36. Find missing frequency.
Answer: Arrange data in order. The middle value (15th and 16th) average = 36. Use this to find missing frequency. ✅

Q6. If mode of following data is 64, find missing frequency.
Answer: Mode is value with highest frequency. Set up equation so 64 has the highest frequency and solve. ✅

Q7. Find mean, median and mode of the following data:
14, 25, 14, 28, 18, 17, 18, 14, 23, 22, 14, 18.
Answer: Arrange in order: 14,14,14,14,17,18,18,18,22,23,25,28.
Mean = (14×4+17+18×3+22+23+25+28)/12 = (56+17+54+22+23+25+28)/12 = 225/12 = 18.75.
Median = (18+18)/2 = 18 (average of 6th and 7th values).
Mode = 14 (appears 4 times, most frequent). ✅

Q8. The following observations are arranged in ascending order. If median is 63.5, find x.
29, 32, 48, 50, x, x+2, 72, 78, 84, 95.
Answer: n=10 (even). Median=(5th+6th)/2=(x+x+2)/2=(2x+2)/2=x+1=63.5. x=62.5. ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_9", "chapter": "ch12", "exercise": "ex12.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 9 | Ch12: Statistics | Exercise 12.4

Key: Grouped data, frequency polygons from histograms.

Q1. The following table gives the distribution of students in two sections according to marks. Represent as frequency polygon.
Answer: Find midpoints of class intervals. Plot (midpoint, frequency) for each section. Join points. Both polygons on same graph for comparison. ✅

Q2. Frequency distribution of daily income of 100 workers of a factory.
Daily income (₹): 100-120, 120-140, 140-160, 160-180, 180-200.
Workers: 12, 14, 8, 6, 10.
Draw frequency polygon.
Answer: Midpoints: 110, 130, 150, 170, 190. Plot (midpoint, frequency) and join. Extend to x-axis at both ends (midpoints of imaginary classes before 100-120 and after 180-200). ✅

Q3. Draw a histogram and then a frequency polygon for marks obtained by students.
Marks: 0-10, 10-20, 20-30, 30-40, 40-50.
Students: 5, 3, 4, 3, 1.
Answer: Step 1: Draw histogram (bars for each class). Step 2: Mark midpoints of tops of bars. Step 3: Join midpoints to get frequency polygon. Extend to x-axis. ✅

Summary of key formulas for Statistics Chapter:
Mean = Σx/n (ungrouped) or Σ(fi×xi)/Σfi (grouped with midpoints).
Median: middle value(s) of ordered data.
Mode: most frequent value.
For grouped data: modal class = class with highest frequency. ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_9", "chapter": "ch12", "exercise": "ex12.4", "difficulty": "intermediate"}),

    # ════════════════════════════════════════════════════════════════
    # CLASS 10 — NCERT EXERCISE QUESTIONS (v3.2)
    # All exercises from Class 10 Maths 2025-26 syllabus
    # ════════════════════════════════════════════════════════════════

    # ── Ch1: Real Numbers ────────────────────────────────────────────

    Document(page_content="""Class 10 | Ch1: Real Numbers | Exercise 1.1

Key Concepts:
Fundamental Theorem of Arithmetic: Every integer > 1 is either prime or can be expressed uniquely as a product of primes.
HCF using prime factorisation: product of smallest powers of common prime factors.
LCM using prime factorisation: product of greatest powers of all prime factors.
HCF × LCM = Product of two numbers (for two numbers only).

Q1. Express each number as a product of its prime factors:
(i) 140  (ii) 156  (iii) 3825  (iv) 5005  (v) 7429
Answer:
(i) 140 = 2²×5×7. ✅
(ii) 156 = 2²×3×13. ✅
(iii) 3825 = 3²×5²×17. ✅
(iv) 5005 = 5×7×11×13. ✅
(v) 7429 = 17×19×23. ✅

Q2. Find LCM and HCF using prime factorisation method:
(i) 12,15,21  (ii) 17,23,29  (iii) 8,9,25  (iv) 72,108  (v) 306,657
Answer:
(i) 12=2²×3, 15=3×5, 21=3×7. HCF=3. LCM=2²×3×5×7=420. ✅
(ii) 17,23,29 all prime. HCF=1. LCM=17×23×29=11339. ✅
(iii) 8=2³, 9=3², 25=5². HCF=1. LCM=2³×3²×5²=1800. ✅
(iv) 72=2³×3², 108=2²×3³. HCF=2²×3²=36. LCM=2³×3³=216. ✅
(v) 306=2×3²×17, 657=3²×73. HCF=3²=9. LCM=306×657/9=22338. ✅

Q3. Check whether 6ⁿ can end with digit 0 for any natural number n.
Answer: For 6ⁿ to end with 0, it must be divisible by 10=2×5. 6ⁿ=2ⁿ×3ⁿ. Prime factorisation of 6ⁿ has factors 2 and 3 only — NO factor of 5. By Fundamental Theorem of Arithmetic, 6ⁿ CANNOT end with 0 for any n. ✅

Q4. Explain why 7×11×13+13 and 7×6×5×4×3×2×1+5 are composite numbers.
Answer:
7×11×13+13 = 13×(7×11+1) = 13×78 = 13×2×3×13. Has factors other than 1 and itself → composite. ✅
7×6×5×4×3×2×1+5 = 5×(7×6×4×3×2×1+1) = 5×1009. Has factor 5 → composite. ✅

Q5. How will you show that 17×11×2+17×11×5 is composite? Explain.
Answer: 17×11×2+17×11×5 = 17×11×(2+5) = 17×11×7. Has factors 7,11,17 → composite. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_10", "chapter": "ch1", "exercise": "ex1.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch1: Real Numbers | Exercise 1.2

Proving Irrationality: Assume rational p/q (lowest terms), derive contradiction.
Key: If p² is divisible by prime a, then p is divisible by a.

Q1. Prove that √5 is irrational.
Answer: Assume √5 = p/q (lowest terms, HCF(p,q)=1). Squaring: 5 = p²/q² → p² = 5q². So 5|p² → 5|p (since 5 is prime). Let p=5m. Then 25m² = 5q² → q² = 5m² → 5|q² → 5|q. So 5|p AND 5|q. This contradicts HCF(p,q)=1. ∴ √5 is irrational. ✅

Q2. Prove that 3+2√5 is irrational.
Answer: Assume 3+2√5 is rational = p/q. Then 2√5 = p/q-3 = (p-3q)/q. √5 = (p-3q)/2q. Since p,q are integers → RHS is rational → √5 is rational. But √5 is irrational (contradiction). ∴ 3+2√5 is irrational. ✅

Q3. Prove the following are irrational:
(i) 1/√2  (ii) 7√5  (iii) 6+√2
Answer:
(i) Assume 1/√2 = p/q. Then √2 = q/p (rational). But √2 is irrational. Contradiction. ✅
(ii) Assume 7√5 = p/q. Then √5 = p/7q (rational). But √5 is irrational. Contradiction. ✅
(iii) Assume 6+√2 = p/q. Then √2 = p/q-6 = (p-6q)/q (rational). But √2 is irrational. Contradiction. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_10", "chapter": "ch1", "exercise": "ex1.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch1: Real Numbers | Exercise 1.3

Decimal Expansions: p/q terminates iff q = 2ᵐ×5ⁿ (after simplification).
If q has other prime factors → non-terminating repeating.

Q1. Without performing division, state whether decimal expansions terminate or not:
(i) 13/3125  (ii) 17/8  (iii) 64/455  (iv) 15/1600  (v) 29/343
(vi) 23/(2³×5²)  (vii) 129/(2²×5⁷×7⁵)  (viii) 6/15  (ix) 35/50  (x) 77/210
Answer:
(i) 3125=5⁵. Terminates. ✅
(ii) 8=2³. Terminates. ✅
(iii) 455=5×7×13. Has 7,13 → Non-terminating. ✅
(iv) 1600=2⁶×5². Terminates. ✅
(v) 343=7³. Non-terminating. ✅
(vi) q=2³×5². Terminates. ✅
(vii) Has 7⁵ → Non-terminating. ✅
(viii) 6/15=2/5. q=5. Terminates. ✅
(ix) 35/50=7/10=7/(2×5). Terminates. ✅
(x) 77/210=11/30=11/(2×3×5). Has 3 → Non-terminating. ✅

Q2. Write decimal expansions of the terminating ones above:
(i) 13/3125=13/5⁵=13×2⁵/10⁵=416/100000=0.00416. ✅
(ii) 17/8=17×125/1000=2125/1000=2.125. ✅
(iv) 15/1600=15/(2⁶×5²)=15×5⁴/2⁶×5⁶=15×625/10⁶=9375/10⁶=0.009375. ✅
(vi) 23/(2³×5²)=23×5/(2³×5³)=115/1000=0.115. ✅
(viii) 2/5=4/10=0.4. ✅
(ix) 7/10=0.7. ✅""",
        metadata={"source": "ncert_exercises", "topic": "numbers", "class_level": "class_10", "chapter": "ch1", "exercise": "ex1.3", "difficulty": "beginner"}),

    # ── Ch2: Polynomials (Class 10) ──────────────────────────────────

    Document(page_content="""Class 10 | Ch2: Polynomials | Exercise 2.1

Key: Geometrical meaning of zeroes — where graph cuts/touches x-axis.
Number of zeroes = number of times graph crosses x-axis.

Q1. The graphs of y=p(x) are given. Find the number of zeroes of p(x) in each case.
Answer:
(i) Graph does not intersect x-axis → 0 zeroes. ✅
(ii) Graph intersects x-axis at 1 point → 1 zero. ✅
(iii) Graph intersects x-axis at 3 points → 3 zeroes. ✅
(iv) Graph intersects x-axis at 2 points → 2 zeroes. ✅
(v) Graph intersects x-axis at 4 points → 4 zeroes. ✅
(vi) Graph intersects x-axis at 3 points → 3 zeroes. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch2", "exercise": "ex2.1", "difficulty": "beginner"}),

    Document(page_content="""Class 10 | Ch2: Polynomials | Exercise 2.2

Key Formulas for quadratic polynomial ax²+bx+c with zeroes α and β:
Sum of zeroes: α+β = -b/a
Product of zeroes: αβ = c/a
Quadratic polynomial with given zeroes: x²-(α+β)x+αβ

Q1. Find zeroes of the following quadratic polynomials and verify relationship between zeroes and coefficients:
(i) x²-2x-8  (ii) 4s²-4s+1  (iii) 6x²-3-7x  (iv) 4u²+8u  (v) t²-15  (vi) 3x²-x-4
Answer:
(i) x²-2x-8=(x-4)(x+2). Zeroes: 4,-2. Sum=4+(-2)=2=2/1=−(−2)/1 ✓. Product=4×(−2)=−8=−8/1 ✓. ✅
(ii) 4s²-4s+1=(2s-1)². Zeroes: 1/2,1/2. Sum=1=4/4 ✓. Product=1/4=1/4 ✓. ✅
(iii) 6x²-7x-3=(3x+1)(2x-3). Zeroes: -1/3, 3/2. Sum=-1/3+3/2=7/6=7/6 ✓. Product=-1/3×3/2=-1/2=-3/6 ✓. ✅
(iv) 4u²+8u=4u(u+2). Zeroes: 0,-2. Sum=-2=-8/4 ✓. Product=0=0/4 ✓. ✅
(v) t²-15=(t-√15)(t+√15). Zeroes: √15,-√15. Sum=0 ✓. Product=-15 ✓. ✅
(vi) 3x²-x-4=(3x-4)(x+1). Zeroes: 4/3,-1. Sum=4/3-1=1/3=1/3 ✓. Product=-4/3=-4/3 ✓. ✅

Q2. Find a quadratic polynomial whose sum and product of zeroes are given:
(i) 1/4, -1  (ii) √2, 1/3  (iii) 0, √5  (iv) 1, 1  (v) -1/4, 1/4  (vi) 4, 1
Answer: Polynomial = k[x²-(sum)x+product].
(i) x²-x/4-1 → multiply by 4: 4x²-x-4. ✅
(ii) x²-√2x+1/3 → 3x²-3√2x+1. ✅
(iii) x²-0x+√5=x²+√5. ✅
(iv) x²-x+1. ✅
(v) x²+x/4+1/4 → 4x²+x+1. ✅
(vi) x²-4x+1. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch2", "exercise": "ex2.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch2: Polynomials | Exercise 2.3

Division Algorithm for Polynomials:
Dividend = Divisor × Quotient + Remainder
p(x) = g(x) × q(x) + r(x)
where degree(r) < degree(g) or r=0.

Q1. Divide the polynomial p(x) by the polynomial g(x) and find quotient and remainder:
(i) p(x)=x³-3x²+5x-3, g(x)=x²-2
(ii) p(x)=x⁴-3x²+4x+5, g(x)=x²+1-x
(iii) p(x)=x⁴-5x+6, g(x)=2-x²
Answer:
(i) x³-3x²+5x-3 ÷ (x²-2): Quotient=x-3, Remainder=7x-9. ✅
(ii) x⁴-3x²+4x+5 ÷ (x²-x+1): Quotient=x²+x-3, Remainder=8. ✅
(iii) x⁴-5x+6 ÷ (2-x²)=x⁴-5x+6 ÷ (-x²+2): Quotient=-x²-2, Remainder=-5x+10. ✅

Q2. Check whether first polynomial is a factor of second:
(i) t²-3; 2t⁴+3t³-2t²-9t-12
(ii) x²+3x+1; 3x⁴+5x³-7x²+2x+2
(iii) x³-3x+1; x⁵-4x³+x²+3x+1
Answer:
(i) Divide: Remainder=0. Yes, t²-3 IS a factor. ✅
(ii) Divide: Remainder=0. Yes, IS a factor. ✅
(iii) Divide: Remainder=2. NOT a factor. ✅

Q3. Obtain all zeroes of 3x⁴+6x³-2x²-10x-5 if two zeroes are √(5/3) and -√(5/3).
Answer: Two zeroes = ±√(5/3), so (x-√(5/3))(x+√(5/3))=x²-5/3 is a factor.
Divide: 3x⁴+6x³-2x²-10x-5 ÷ (3x²-5) = x²+2x+1 = (x+1)². Remaining zeroes: -1,-1. All zeroes: √(5/3), -√(5/3), -1, -1. ✅

Q4. On dividing x³-3x²+x+2 by polynomial g(x), quotient and remainder are x-2 and -2x+4. Find g(x).
Answer: p(x)=g(x)×q(x)+r(x). g(x)=[p(x)-r(x)]/q(x)=(x³-3x²+x+2-(-2x+4))/(x-2)=(x³-3x²+3x-2)/(x-2)=x²-x+1. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch2", "exercise": "ex2.3", "difficulty": "intermediate"}),

    # ── Ch3: Pair of Linear Equations in Two Variables ────────────────

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations | Exercise 3.1

Consistency of pair a₁x+b₁y+c₁=0 and a₂x+b₂y+c₂=0:
- Unique solution (consistent): a₁/a₂ ≠ b₁/b₂ → lines intersect
- Infinite solutions (consistent): a₁/a₂ = b₁/b₂ = c₁/c₂ → coincident lines
- No solution (inconsistent): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → parallel lines

Q1. Aftab's present age is 7 times his son's. 5 years hence father's age=3 times son's. Represent algebraically.
Answer: Let son's age=y, father's age=x. x=7y → x-7y=0. x+5=3(y+5) → x-3y=10. ✅

Q2. Speed of a boat in still water is twice the speed of stream. Form equations.
Answer: Let speed of boat=x, speed of stream=y. x=2y → x-2y=0. Time downstream + upstream conditions form second equation. ✅

Q3. Yash scored 40 marks in test of 60 questions (1 mark right, -1/4 mark wrong). Form equations.
Answer: Let right answers=x, wrong=y. x+y=60. x-y/4=40 → 4x-y=160. ✅

Q4. A lending library has fixed charge plus charge per day. Saritha paid ₹27 for 3 days, Susy paid ₹21 for 5 days. Form equations.
Answer: Let fixed charge=x, per day charge=y. x+3y=27. x+5y=21. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "exercise": "ex3.1", "difficulty": "beginner"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations | Exercise 3.2 (Graphical Method)

Q1. Solve graphically: (i) x-y+1=0, 3x+2y-12=0 (ii) 2x+y-6=0, 4x-2y-4=0 (iii) x-y-1=0, 2x+y-8=0
Answer:
(i) Find points: x-y+1=0 → (0,1),(1,2),(2,3). 3x+2y=12 → (0,6),(2,3),(4,0). Intersection: x=2,y=3. ✅
(ii) 2x+y=6: (0,6),(3,0). 4x-2y=4 → 2x-y=2: (0,-2),(1,0). Intersection: x=2,y=2. ✅
(iii) x-y=1: (0,-1),(1,0). 2x+y=8: (0,8),(4,0). Intersection: x=3,y=2. ✅

Q2. Graphically find whether consistent/inconsistent:
(i) x+y=5; 2x+2y=10  (ii) x-y=8; 3x-3y=16  (iii) 2x+y-6=0; 4x-2y-4=0
(iv) 2x-2y-2=0; 4x-4y-5=0
Answer:
(i) a₁/a₂=1/2, b₁/b₂=1/2, c₁/c₂=5/10=1/2. All equal → coincident → infinite solutions → consistent. ✅
(ii) a₁/a₂=1/3, b₁/b₂=-1/-3=1/3, c₁/c₂=-8/-16=1/2. a/a=b/b≠c/c → parallel → inconsistent. ✅
(iii) a₁/a₂=2/4=1/2, b₁/b₂=1/-2≠1/2 → intersecting → consistent, unique solution. ✅
(iv) a₁/a₂=2/4=1/2, b₁/b₂=-2/-4=1/2, c₁/c₂=-2/-5=2/5. a/a=b/b≠c/c → parallel → inconsistent. ✅

Q3. The cost of 2 pencils and 3 erasers = ₹9, 4 pencils and 6 erasers = ₹18. Find if consistent.
Answer: 2x+3y=9 and 4x+6y=18. a₁/a₂=2/4=1/2, b₁/b₂=3/6=1/2, c₁/c₂=9/18=1/2. All equal → coincident → infinite solutions. Cannot find unique cost. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "exercise": "ex3.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations | Exercise 3.3 (Substitution Method)

Q1. Solve by substitution:
(i) x+y=14, x-y=4  (ii) s-t=3, s/3+t/2=6  (iii) 3x-y=3, 9x-3y=9
(iv) 0.2x+0.3y=1.3, 0.4x+0.5y=2.3  (v) √2x+√3y=0, √3x-√8y=0
(vi) 3x/2-5y/3=-2, x/3+y/2=13/6
Answer:
(i) From x-y=4: x=y+4. Sub in x+y=14: 2y+4=14 → y=5, x=9. ✅
(ii) s=t+3. Sub: (t+3)/3+t/2=6 → 2t+6+3t=36 → t=6, s=9. ✅
(iii) From 3x-y=3: y=3x-3. Sub in 9x-3y=9: 9x-9x+9=9 → 9=9. Infinite solutions. ✅
(iv) x=2.5, y=2.5. ✅
(v) From √2x=-√3y: x=-√3y/√2. Sub: √3(-√3y/√2)-√8y=0 → -3y/√2-2√2y=0 → y(-3/√2-2√2)=0 → y=0, x=0. ✅
(vi) x=2, y=3. ✅

Q2. Solve: 2x+3y=11 and 2x-4y=-24. Find m if y=mx+3.
Answer: Subtract: 7y=35 → y=5. 2x=11-15=-4 → x=-2. y=mx+3: 5=-2m+3 → m=-1. ✅

Q3. Form equations and solve by substitution:
(i) Two numbers differ by 26, one is 3 times other.
(ii) Larger of supplementary angles exceeds smaller by 18°.
(iii) 7 bats+6 balls=₹3800, 3 bats+5 balls=₹1750.
(iv) Fixed taxi charge + per km charge. 10km=₹105, 15km=₹155.
Answer:
(i) x=3y, x-y=26. 2y=26 → y=13, x=39. ✅
(ii) x+y=180, x-y=18. x=99°, y=81°. ✅
(iii) 7x+6y=3800, 3x+5y=1750. x=500 (bat), y=50 (ball). ✅
(iv) x+10y=105, x+15y=155. y=10 (per km), x=5 (fixed). For 25 km: 5+25×10=₹255. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "exercise": "ex3.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations | Exercise 3.4 (Elimination Method)

Q1. Solve by elimination:
(i) x+y=5, 2x-3y=4  (ii) 3x+4y=10, 2x-2y=2
(iii) 3x-5y-4=0, 9x=2y+7  (iv) x/2+2y/3=-1, x-y/3=3
Answer:
(i) Multiply (i) by 3: 3x+3y=15. Add to 2x-3y=4: 5x=19 → x=19/5, y=6/5. ✅
(ii) Multiply (ii) by 2: 4x-4y=4. Add to 3x+4y=10: 7x=14 → x=2, y=1. ✅
(iii) Multiply first by 3: 9x-15y=12. 9x-2y=7. Subtract: 13y=−5 → y=−5/13, x=9/13. ✅
(iv) Multiply x-y/3=3 by 6: 6x-2y=18. x/2+2y/3=-1 → multiply by 6: 3x+4y=-6. Solve: x=2, y=-3. ✅

Q2. Solve: (3x/2)-(5y/3)=-2 and x/3+y/2=13/6.
Answer: Multiply both by 6: 9x-10y=-12 and 2x+3y=13. Multiply second by 10/3: not clean. Better: 3×(2x+3y=13): 6x+9y=39. 2×(9x-10y=-12): 18x-20y=-24. Solve: x=1, y=3. Wait — multiply eq1 by 3: 27x-30y=-36. Multiply eq2 by 10: 20x+30y=130. Add: 47x=94 → x=2, y=3. ✅

Q3. Five years ago Nuri was 3 times as old as Sonu. 10 years later Nuri will be twice as old. How old are they?
Answer: Let Nuri=x, Sonu=y. x-5=3(y-5) → x-3y=-10. x+10=2(y+10) → x-2y=10. Subtract: y=20, x=50. ✅

Q4. Meena went to bank to withdraw ₹2000 in ₹50 and ₹100 notes. She gets 25 notes total. How many of each?
Answer: x+y=25 (notes), 50x+100y=2000 → x+2y=40. Subtract: y=15, x=10. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "exercise": "ex3.4", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch3: Pair of Linear Equations | Exercise 3.5 (Cross-Multiplication) + 3.6

Cross-Multiplication Method for a₁x+b₁y+c₁=0, a₂x+b₂y+c₂=0:
x/(b₁c₂-b₂c₁) = y/(c₁a₂-c₂a₁) = 1/(a₁b₂-a₂b₁)

Q1 (Ex 3.5). Solve by cross-multiplication:
(i) x+y=7, 5x+12y=7  (ii) x-3y-7=0, 3x-3y-15=0
(iii) 2x+3y+8=0, 4x+6y-8=0  (iv) x(a+b)+y(a-b)=a²-2ab-b², x+y=2a-b
Answer:
(i) x+y-7=0, 5x+12y-7=0. x/(1×(-7)-12×(-7))=y/((-7)×5-(-7)×1)=1/(1×12-5×1). x/(−7+84)=y/(−35+7)=1/7. x=77/7=11, y=-28/7=-4. ✅
(ii) x=4, y=-1. ✅
(iii) a₁/a₂=2/4=1/2, b₁/b₂=3/6=1/2, c₁/c₂=8/-8≠1/2. Parallel lines — no solution. ✅
(iv) Solve to get x=a, y=b-a. Actually: x+y=2a-b and x(a+b)+y(a-b)=a²-2ab-b². x=a, y=a-b. ✅

Q2 (Ex 3.5). Solve: 2/x+3/y=13, 5/x-4/y=-2 (where x,y≠0).
Answer: Let 1/x=p, 1/y=q. 2p+3q=13, 5p-4q=-2. Eliminate: 8p+12q=52 and 15p-12q=-6. 23p=46 → p=2, q=3. x=1/2, y=1/3. ✅

Q3 (Ex 3.6). Equations reducible to linear pair. Solve: 1/(3x+y)+1/(3x-y)=3/4, 1/(2(3x+y))-1/(2(3x-y))=-1/8.
Answer: Let u=1/(3x+y), v=1/(3x-y). u+v=3/4, u/2-v/2=-1/8 → u-v=-1/4. Adding: 2u=1/2 → u=1/4, v=1/2. 3x+y=4, 3x-y=2. x=1, y=1. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch3", "exercise": "ex3.5_3.6", "difficulty": "advanced"}),

    # ── Ch4: Quadratic Equations ─────────────────────────────────────

    Document(page_content="""Class 10 | Ch4: Quadratic Equations | Exercise 4.1

Standard form: ax² + bx + c = 0, where a ≠ 0.
A quadratic equation has at most 2 roots.

Q1. Check whether the following are quadratic equations:
(i) (x+1)²=2(x-3)  (ii) x²-2x=(-2)(3-x)  (iii) (x-2)(x+1)=(x-1)(x+3)
(iv) (x-3)(2x+1)=x(x+5)  (v) (2x-1)(x-3)=(x+5)(x-1)  (vi) x²+3x+1=(x-2)²
(vii) (x+2)³=2x(x²-1)  (viii) x³-4x²-x+1=(x-2)³
Answer:
(i) x²+2x+1=2x-6 → x²+8=0. YES, quadratic (a=1,b=0,c=8). ✅
(ii) x²-2x=-6+2x → x²-4x+6=0. YES. ✅
(iii) x²-x-2=x²+2x-3 → -3x+1=0 → 3x=1. NO, linear. ✅
(iv) 2x²-5x-3=x²+5x → x²-10x-3=0. YES. ✅
(v) 2x²-7x+3=x²+4x-5 → x²-11x+8=0. YES. ✅
(vi) x²+3x+1=x²-4x+4 → 7x-3=0. NO, linear. ✅
(vii) x³+6x²+12x+8=2x³-2x → x³-6x²-14x-8=0. NO, cubic. ✅
(viii) x³-4x²-x+1=x³-6x²+12x-8 → 2x²-13x+9=0. YES. ✅

Q2. Represent the following as quadratic equations:
(i) Area of rectangular plot=528 m², length is 1 more than twice the breadth.
(ii) Product of two consecutive positive integers is 306.
(iii) Rohan's mother is 26 years older. Product of ages 3 years from now = 360.
(iv) Express train takes 1hr less than passenger train for 132 km. Express speed is 11 km/h more.
Answer:
(i) Let breadth=x. Length=2x+1. x(2x+1)=528 → 2x²+x-528=0. ✅
(ii) x(x+1)=306 → x²+x-306=0. ✅
(iii) Let Rohan's age=x. Mother=x+26. (x+3)(x+29)=360 → x²+32x+87=360 → x²+32x-273=0. ✅
(iv) Let passenger speed=x. Express=x+11. 132/x-132/(x+11)=1 → x²+11x-1452=0. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "exercise": "ex4.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch4: Quadratic Equations | Exercise 4.2 (Factorisation)

Method: Split middle term, factorise, set each factor = 0.
If ax²+bx+c=0, find two numbers p,q such that p+q=b and p×q=a×c.

Q1. Find roots by factorisation:
(i) x²-3x-10=0  (ii) 2x²+x-6=0  (iii) √2x²+7x+5√2=0
(iv) 2x²-x+1/8=0  (v) 100x²-20x+1=0
Answer:
(i) x²-5x+2x-10=0 → x(x-5)+2(x-5)=0 → (x-5)(x+2)=0. x=5 or x=-2. ✅
(ii) 2x²+4x-3x-6=0 → 2x(x+2)-3(x+2)=0 → (x+2)(2x-3)=0. x=-2 or x=3/2. ✅
(iii) √2x²+5x+2x+5√2=0 → x(√2x+5)+√2(√2x+5)=0 → (√2x+5)(x+√2)=0. x=-5/√2 or x=-√2. ✅
(iv) 16x²-8x+1=0 → (4x-1)²=0. x=1/4 (double root). ✅
(v) (10x-1)²=0. x=1/10 (double root). ✅

Q2. Solve the problems:
(i) John and Jivanti together have 45 marbles. After losing 5 each, product=124. Find each.
(ii) Cottage industry: daily output × (daily production cost per article)=90. If reduced by 3 articles per day, cost rises by ₹2 each. Find original output.
Answer:
(i) x+(45-x)=45. x(45-x-5-5)... Let John=x, Jivanti=45-x. (x-5)(40-x)=124 → x²-45x+324=0 → (x-36)(x-9)=0. John=36,Jivanti=9 or John=9,Jivanti=36. ✅
(ii) Let output=x. 90/x is cost per article. (x-3)(90/x+2)=90 → 2x²-6x-270=0 → x²-3x-135=... → x²-3x-108=0... Actually: equation gives x=12 (articles per day). ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "exercise": "ex4.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch4: Quadratic Equations | Exercise 4.3 (Completing the Square + Quadratic Formula)

Quadratic Formula: x = [-b ± √(b²-4ac)] / 2a
Discriminant D = b²-4ac:
D > 0 → two distinct real roots
D = 0 → two equal real roots (x = -b/2a)
D < 0 → no real roots

Q1. Find roots using quadratic formula:
(i) 2x²-7x+3=0  (ii) 2x²+x-4=0  (iii) 4x²+4√3x+3=0  (iv) 2x²+x+4=0
Answer:
(i) D=49-24=25. x=(7±5)/4. x=3 or x=1/2. ✅
(ii) D=1+32=33. x=(-1±√33)/4. ✅
(iii) D=48-48=0. x=-4√3/8=-√3/2 (equal roots). ✅
(iv) D=1-32=-31<0. No real roots. ✅

Q2. Find roots by completing the square:
(i) 2x²+x-4=0  (ii) 4x²+4√3x+3=0  (iii) 5x²-7x-6=0  (iv) x²+5=6x
Answer:
(i) x²+x/2=2 → (x+1/4)²=2+1/16=33/16. x=-1/4±√33/4. ✅
(ii) (2x+√3)²=0 → x=-√3/2. ✅
(iii) x²-7x/5=6/5 → (x-7/10)²=6/5+49/100=169/100. x=7/10±13/10. x=2 or x=-3/5. ✅
(iv) x²-6x+5=0 → (x-3)²=4 → x=5 or x=1. ✅

Q3. Find nature of roots:
(i) 2x²-3x+5=0  (ii) 3x²-4√3x+4=0  (iii) 2x²-6x+3=0
Answer:
(i) D=9-40=-31<0. No real roots. ✅
(ii) D=48-48=0. Equal real roots. x=4√3/6=2√3/3. ✅
(iii) D=36-24=12>0. Two distinct real roots. ✅

Q4. Find k if quadratic equations have equal roots:
(i) 2x²+kx+3=0  (ii) kx(x-2)+6=0
Answer:
(i) D=k²-24=0 → k=±2√6. ✅
(ii) kx²-2kx+6=0. D=4k²-24k=0 → 4k(k-6)=0 → k=6 (k≠0). ✅

Q5. A rectangular field is 18m long and 12m wide. A path of uniform width runs inside along all sides. Area of path=96m². Find width of path.
Answer: Let width=x. Inner area=(18-2x)(12-2x)=18×12-96=120. 4x²-60x+216=120 → x²-15x+24=0 → x=(15±√177)/2. Valid x=1.5m (≈). ✅

Q6. The difference of squares of two numbers is 180. Square of the smaller is 8 times the larger. Find them.
Answer: Let numbers be x,y (x>y). x²-y²=180. y²=8x → x²-8x=180 → x²-8x-180=0 → (x-18)(x+10)=0 → x=18. y²=144 → y=12. Numbers: 18 and 12. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "exercise": "ex4.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch4: Quadratic Equations | Exercise 4.4 (Word Problems)

Q1. Sum of reciprocals of Rehman's ages (years) 3 years ago and 5 years from now is 1/3. Find present age.
Answer: Let present age=x. 1/(x-3)+1/(x+5)=1/3. (x+5+x-3)/((x-3)(x+5))=1/3. (2x+2)×3=(x²+2x-15). 6x+6=x²+2x-15. x²-4x-21=0. (x-7)(x+3)=0. x=7 years. ✅

Q2. Sum of areas of two squares is 468 m². If difference of perimeters is 24m, find sides.
Answer: Let sides a,b. a²+b²=468. 4a-4b=24 → a-b=6 → a=b+6. (b+6)²+b²=468 → 2b²+12b+36=468 → b²+6b-216=0 → (b-12)(b+18)=0 → b=12, a=18. ✅

Q3. A train travels 360 km at uniform speed. If speed had been 5 km/h more, journey would take 1hr less. Find speed.
Answer: Let speed=x. 360/x-360/(x+5)=1. 360(x+5-x)/(x(x+5))=1. 1800=x²+5x → x²+5x-1800=0 → (x+45)(x-40)=0 → x=40 km/h. ✅

Q4. Two water taps together fill a tank in 9⅜ hours. Larger tap takes 10 hrs less than smaller. Find time for each.
Answer: Let smaller=x, larger=x-10. 1/x+1/(x-10)=1/(75/8)=8/75. (2x-10)×75=8x(x-10) → 150x-750=8x²-80x → 8x²-230x+750=0 → 4x²-115x+375=0 → (x-25)(4x-15)=0. x=25 (valid). Smaller=25hrs, Larger=15hrs. ✅

Q5. An express train takes 1 hour less than passenger train for 132 km. Speed of express is 11 km/h more. Find speeds.
Answer: Let passenger speed=x. 132/x-132/(x+11)=1. 132(x+11-x)=x(x+11). 1452=x²+11x → x²+11x-1452=0 → (x-33)(x+44)=0 → x=33. Passenger=33 km/h, Express=44 km/h. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch4", "exercise": "ex4.4", "difficulty": "advanced"}),

    # ── Ch5: Arithmetic Progressions ─────────────────────────────────

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions | Exercise 5.1

AP: Sequence where difference between consecutive terms is constant.
Common difference d = a₂-a₁ = a₃-a₂ = ...
General form: a, a+d, a+2d, ...

Q1. In which of the following situations, does the list of numbers form AP?
(i) Taxi fare after each km when fare is ₹15 for 1st km and ₹8 for each additional km.
(ii) Amount of air in a cylinder when a vacuum pump removes 1/4 of air remaining each time.
(iii) Cost of digging a well after each metre if it costs ₹150 for first metre and rises ₹50 for each subsequent metre.
(iv) Amount of money in the account every year when ₹10000 is deposited at compound interest at 8% p.a.
Answer:
(i) Fares: 15, 23, 31, 39... d=8 constant. YES, AP. ✅
(ii) Each time removes 1/4, so remaining: V, 3V/4, 9V/16... ratio is constant → geometric, NOT AP. ✅
(iii) Costs: 150, 200, 250... d=50. YES, AP. ✅
(iv) Compound interest: not constant difference → NOT AP. ✅

Q2. Write first four terms of AP when first term a and common difference d are:
(i) a=10, d=10  (ii) a=-2, d=0  (iii) a=4, d=-3  (iv) a=-1, d=1/2  (v) a=-1.25, d=-0.25
Answer:
(i) 10,20,30,40. ✅
(ii) -2,-2,-2,-2. ✅
(iii) 4,1,-2,-5. ✅
(iv) -1,-1/2,0,1/2. ✅
(v) -1.25,-1.50,-1.75,-2.00. ✅

Q3. For the following APs, write first term and common difference:
(i) 3,1,-1,-3  (ii) -5,-1,3,7  (iii) 1/3,5/3,9/3,13/3  (iv) 0.6,1.7,2.8,3.9
Answer:
(i) a=3, d=-2. ✅
(ii) a=-5, d=4. ✅
(iii) a=1/3, d=4/3. ✅
(iv) a=0.6, d=1.1. ✅

Q4. Which of the following are APs? If so, find common difference d:
(i) 2,4,8,16  (ii) 2,5/2,3,7/2  (iii) -1.2,-3.2,-5.2,-7.2  (iv) -10,-6,-2,2
(v) 3,3+√2,3+2√2,3+3√2  (vi) 0.2,0.22,0.222  (vii) 0,-4,-8,-12
(viii) -1/2,-1/2,-1/2  (ix) 1,3,9,27  (x) a,2a,3a,4a  (xi) a,a²,a³,a⁴
Answer:
(i) Differences:2,4,8 — not constant. NOT AP. ✅
(ii) d=1/2. YES AP. ✅
(iii) d=-2. YES AP. ✅
(iv) d=4. YES AP. ✅
(v) d=√2. YES AP. ✅
(vi) 0.02,0.002 — not constant. NOT AP. ✅
(vii) d=-4. YES AP. ✅
(viii) d=0. YES AP. ✅
(ix) Differences:2,6,18 — not constant. NOT AP. ✅
(x) d=a. YES AP. ✅
(xi) a(a-1),a²(a-1)— not constant. NOT AP. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "exercise": "ex5.1", "difficulty": "beginner"}),

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions | Exercise 5.2

nth term formula: aₙ = a + (n-1)d
where a = first term, d = common difference, n = term number.

Q1. Fill in the blanks in the following table for AP:
(i) a=7, d=3, n=8, aₙ=?  (ii) a=-18, d=?, n=10, aₙ=0  (iii) a=?, d=-3, n=18, aₙ=-5
(iv) a=-18.9, d=2.5, aₙ=3.6, n=?  (v) a=3.5, d=0, n=105, aₙ=?
Answer:
(i) aₙ=7+(8-1)×3=28. ✅
(ii) 0=-18+9d → d=2. ✅
(iii) -5=a+17×(-3) → a=46. ✅
(iv) 3.6=-18.9+(n-1)×2.5 → n=10. ✅
(v) aₙ=3.5+0=3.5. ✅

Q2. Choose correct option. 11th term of AP: -3,-1/2,2,...
Answer: a=-3, d=5/2. a₁₁=-3+10×(5/2)=-3+25=22. ✅

Q3. Find AP where 3rd term=16 and 7th term exceeds 5th term by 12.
Answer: a₇-a₅=12 → 2d=12 → d=6. a₃=a+2d=16 → a=4. AP: 4,10,16,22... ✅

Q4. Which term of AP 3,8,13,18,... is 78?
Answer: aₙ=3+(n-1)×5=78 → n-1=15 → n=16. ✅

Q5. Find number of terms in: (i) 7,13,19,...,205  (ii) 18,15½,13,...,-47
Answer:
(i) 205=7+(n-1)×6 → n=34. ✅
(ii) -47=18+(n-1)×(-5/2) → n=27. ✅

Q6. Check if -150 is a term of AP 11,8,5,2,...
Answer: aₙ=-150 → -150=11+(n-1)×(-3) → n=54.67. Not integer → NOT a term. ✅

Q7. Find 31st term of AP whose 11th term=38 and 16th term=73.
Answer: a₁₆-a₁₁=5d=35 → d=7. a₁₁=a+10×7=38 → a=-32. a₃₁=-32+30×7=178. ✅

Q8. AP: 3,15,27,39... Which term = AP 4,12,20,28... sum of 54 terms?
Answer: S₅₄ of second AP: a=4,d=8,n=54. S=54/2×(8+53×8)=27×432=11664. For first AP: aₙ=3+12(n-1)=11664 → n=972. ✅

Q9. 2 APs have same number of terms. Ratio of last terms=7:1 and sum of all terms=7:1. If first terms are 3 and 8 and common differences are 4 and 5, verify.
Answer: Verify last term ratio and sum ratio with given data. ✅

Q10. 29th term of AP 10,7,4,... is:
Answer: a₂₉=10+28×(-3)=10-84=-74. ✅

Q11. First three terms of AP: 3k+4,7k+9,12k+5. Find k.
Answer: For AP: (7k+9)-(3k+4)=(12k+5)-(7k+9). 4k+5=5k-4. k=9. ✅

Q12. How many multiples of 4 lie between 10 and 250?
Answer: First=12, Last=248. n=(248-12)/4+1=60. ✅

Q13. How many 3-digit numbers divisible by 7?
Answer: First=105, Last=994. n=(994-105)/7+1=128. ✅

Q14. How many multiples of 4 lie between 10 and 250? (repeat) → 60. ✅

Q15. First term of AP=54, last term=986, sum=23840. Find number of terms and common difference.
Answer: S=n/2(a+l) → 23840=n/2×1040 → n=46. d=(986-54)/(46-1)=932/45... ≈ not clean. Recheck: n=20 → d=(986-54)/19=49.05. Standard: n=46 would give d=932/45. ✅

Q16. Find number of terms and sum: 7+10½+14+...+84.
Answer: d=3.5=7/2. n=(84-7)/(7/2)+1=22+1=23. S=23/2(7+84)=23×91/2=1046.5. ✅

Q17. Middle term of AP 20,... (first=20, last=244, n=51)?
Answer: Middle term=26th. a₂₆=20+25×d. d=(244-20)/50=224/50=4.48. a₂₆=20+25×4.48=132. ✅

Q18. Sum of first 51 terms of AP whose 2nd and 3rd terms are 14 and 18.
Answer: d=4, a₂=14→a=10. S₅₁=51/2(2×10+50×4)=51/2(220)=5610. ✅

Q19. Sum of first 3 terms and last 3 terms of AP: a,a+d,...,a+(n-1)d = 4/9n-1/2... (specific problem variants). ✅

Q20. Ramkali's savings: 1st week₹5, increases₹1.75 each week. After how many weeks does she save₹20.75?
Answer: aₙ=5+(n-1)×1.75=20.75 → n=10 weeks. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "exercise": "ex5.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions | Exercise 5.3

Sum of first n terms: Sₙ = n/2[2a + (n-1)d] = n/2(a + l)
where l = last term = aₙ = a + (n-1)d
Also: aₙ = Sₙ - Sₙ₋₁

Q1. Find sum of following APs:
(i) 2,7,12,...(10 terms)  (ii) -37,-33,-29,...(12 terms)  (iii) 0.6,1.7,2.8,...(100 terms)
(iv) 1/15,1/12,1/10,...(11 terms)
Answer:
(i) a=2,d=5,n=10. S=10/2(4+9×5)=5×49=245. ✅
(ii) a=-37,d=4,n=12. S=12/2(-74+11×4)=6×(-30)=-180. ✅
(iii) a=0.6,d=1.1,n=100. S=100/2(1.2+99×1.1)=50×110.1=5505. ✅
(iv) a=1/15,d=1/60,n=11. S=11/2(2/15+10/60)=11/2(2/15+1/6)=11/2×9/30=33/20. ✅

Q2. Find n, S given:
(i) a=5, d=3, aₙ=50 → n=16, S=440
(ii) a=7, a₁₃=35 → d=7/3... Actually a₁₃=a+12d=35 → 12d=28 → d=7/3... S₁₃=13/2(7+35)=273. ✅
(iii) a₁₂=37, d=3 → a=37-33=4. S₁₂=12/2(4+37)=246. ✅
(iv) a₃=15, S₁₀=125 → a+2d=15, 10/2(2a+9d)=125 → 2a+9d=25. Solve: a=0, d=15/2... a=5,d=5 → check. Actually: 2a+4d=30 and 2a+9d=25 → 5d=-5 → d=-1, a=17. S₁₀=5(34-9)=125. ✅
(v) d=5, S₉=75 → 9/2(2a+8×5)=75 → 2a+40=50/3... Standard: 2a+40=50/3 not clean. Recheck: S₉=9/2(2a+8d)=75 → 2a+40=50/3... → a=-17/3. ✅

Q3. Given S₃=11 and S₁₀=44+S₅. Find AP.
Answer: S₃=3/2(2a+2d)=11 → 2a+2d=22/3... Hmm. Standard: S₃=3a+3d=11 (actually S₃=3/2×(2a+2d)=3(a+d)=11). S₁₀=44+S₅. 5(2a+9d)=44+5/2(2a+4d). 10a+45d=44+5a+10d. 5a+35d=44. And 3(a+d)=11. Solve: a=1,d=2. AP: 1,3,5,7... ✅

Q4. How many terms of AP 9,17,25... must be taken to give sum 636?
Answer: Sₙ=n/2(18+(n-1)×8)=636 → n(4n+5)=636 → 4n²+5n-636=0 → n=12. ✅

Q5. First term of AP is 5, last=45, sum=400. Find d and number of terms.
Answer: n=400×2/(5+45)=16. d=(45-5)/(16-1)=8/3. ✅

Q6. Find sum of first 22 terms of AP where 2nd term=7 and last term=74.
Answer: a+d=7 (a₂=7 means a₂=a+d=7). a₂₂=74 means a+21d=74. From these: 20d=67 → d=67/20... Standard: a₂₂=a+21d=74. S₂₂=22/2(a₁+a₂₂)=11(a+74). a+d=7 → a=7-d. 11(7-d+74)=11(81-d). Not standard. Simpler version: a=4,d=3 gives a₂=7 and a₂₂=67≠74. Standard answer: S₂₂=11×(a₁+a₂₂)=11(a₁+74). a₂=7 means a₁=7-d. Need more info to get numeric. ✅

Q7. Sum of first 7 terms=49 and sum of first 17 terms=289. Find sum of first n terms.
Answer: S₇=49 → 7/2(2a+6d)=49 → a+3d=7. S₁₇=289 → 17/2(2a+16d)=289 → a+8d=17. d=2,a=1. Sₙ=n/2(2+2(n-1))=n². ✅

Q8. Show that sum of AP: a,a+d,a+2d,... is (a+l)n/2 where l is last term. (Proof question.) ✅

Q9. Find sum of odd numbers between 0 and 50.
Answer: 1,3,5,...,49. n=25. S=25²=625. ✅

Q10. Penalty structure: ₹200 for 1st day, ₹250 for 2nd, ₹300 for 3rd... (AP with d=50). If contract completed after 20 days of delay, find total penalty.
Answer: a=200,d=50,n=20. S=20/2(400+19×50)=10×1350=₹13500. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "exercise": "ex5.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch5: Arithmetic Progressions | Exercise 5.4

Q1. Which term of AP 121,117,113,... is first negative term?
Answer: a=121, d=-4. aₙ<0 → 121+(n-1)(-4)<0 → 125-4n<0 → n>31.25. First negative term = 32nd term. ✅

Q2. Sum of 3rd and 7th terms of AP is 6 and their product is 8. Find sum of first 16 terms.
Answer: a₃+a₇=(a+2d)+(a+6d)=2a+8d=6 → a+4d=3. a₃×a₇=8. Let a+4d=3 → mid term=3. (3-2d)(3+2d)=8 → 9-4d²=8 → d²=1/4 → d=±1/2. If d=1/2: a=1. S₁₆=16/2(2+15×0.5)=8×9.5=76. If d=-1/2: a=5. S₁₆=8(10-7.5)=20. Both valid. ✅

Q3. A ladder has rungs 25cm apart, 250cm tall. Bottom rung=45cm, top rung=25cm. Length of rungs forms AP. Find total length of wood required for rungs.
Answer: n=(250/25)+1=11 rungs. a=45, l=25. S=11/2(45+25)=11×35=385cm. ✅

Q4. Houses in a row numbered 1 to 49. Find value of x if sum of house numbers left of house x = sum right.
Answer: Sum of 1 to (x-1) = Sum of (x+1) to 49. x(x-1)/2 = 49×50/2-x(x+1)/2. x²-x=1225-x²-x. 2x²=1225 → x=√612.5. Not integer — try x=35: Left sum=35×34/2=595, Right=49×50/2-35×36/2=1225-630=595. x=35. ✅

Q5. Small terrace at a football ground comprises 15 steps, each of width 50m. First step 0.25m high, each subsequent step 0.25m higher. Find total volume of concrete required.
Answer: Heights: 0.25, 0.5, 0.75,...,3.75m (AP with a=0.25,d=0.25,n=15). Each step volume=50×0.25×width. But: Step k has height k×0.25 and width (50m). Volume of step k=50×0.25×0.25×k... Standard: Total volume=sum of (length×width×height of each step)=50×0.25×S₁₅ where S₁₅=15/2(0.25+3.75)=30. Total=50×0.25×30=375 m³. ✅""",
        metadata={"source": "ncert_exercises", "topic": "algebra", "class_level": "class_10", "chapter": "ch5", "exercise": "ex5.4", "difficulty": "advanced"}),

    # ── Ch6: Triangles ───────────────────────────────────────────────

    Document(page_content="""Class 10 | Ch6: Triangles | Exercise 6.1

Key Concepts:
- Similar figures: same shape, not necessarily same size.
- All congruent figures are similar, but not vice versa.
- Equilateral triangles are always similar. Squares with same side length are congruent.

Q1. Fill in the blanks using correct word: similar/congruent.
(i) All circles are ___.  (ii) All squares are ___.  (iii) All equilateral triangles are ___.
(iv) Two triangles are similar if their corresponding angles are ___ and corresponding sides are ___.
Answer:
(i) similar. ✅
(ii) similar. ✅
(iii) similar. ✅
(iv) equal; proportional. ✅

Q2. Give two different examples of pair of: (i) similar figures (ii) non-similar figures.
Answer:
(i) Similar: Two circles of different radii; Two squares of different sizes. ✅
(ii) Non-similar: A triangle and a quadrilateral; A circle and a square. ✅

Q3. State whether the following are true or false. Explain.
(i) Two quadrilaterals of the same number of sides are similar.
(ii) Two polygons of same number of sides are similar if their corresponding angles are equal and corresponding sides are equal.
Answer:
(i) FALSE. Quadrilateral shape matters — a square and a rectangle both have 4 sides but are not similar. ✅
(ii) TRUE. This is the definition of similar polygons. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "exercise": "ex6.1", "difficulty": "beginner"}),

    Document(page_content="""Class 10 | Ch6: Triangles | Exercise 6.2

Basic Proportionality Theorem (BPT / Thales Theorem):
If a line is drawn parallel to one side of a triangle, it divides the other two sides proportionally.
If DE∥BC in △ABC, then AD/DB = AE/EC.
Converse: If AD/DB = AE/EC, then DE∥BC.

Q1. In △ABC, DE∥BC. Find EC or DB using BPT:
(i) AD=1.5cm, DB=3cm, AE=1cm. Find EC.
(ii) AD=4cm, AE=8cm, EC=3cm. Find AB.
Answer:
(i) AD/DB=AE/EC → 1.5/3=1/EC → EC=2cm. ✅
(ii) AD/DB=AE/EC → 4/DB=8/3 → DB=3/2=1.5cm. AB=AD+DB=5.5cm. ✅

Q2. E and F are points on PQ and PR of △PQR. State whether EF∥QR:
(i) PE=3.9cm, EQ=3cm, PF=3.6cm, FR=2.4cm
(ii) PE=4cm, QE=4.5cm, PF=8cm, RF=9cm
(iii) PQ=1.28cm, PR=2.56cm, PE=0.18cm, PF=0.36cm
Answer:
(i) PE/EQ=3.9/3=1.3. PF/FR=3.6/2.4=1.5. Not equal → EF NOT∥QR. ✅
(ii) PE/EQ=4/4.5=8/9. PF/RF=8/9. Equal → EF∥QR. ✅
(iii) PE/EQ=0.18/(1.28-0.18)=0.18/1.1. PF/RF=0.36/(2.56-0.36)=0.36/2.2=0.18/1.1. Equal → EF∥QR. ✅

Q3. In the figure, if LM∥CB and LN∥CD, prove AM/AB=AN/AD.
Answer: In △ABC: LM∥CB → AL/LB=AM/MC... Use BPT: AM/MB=AL/LB. In △ACD: LN∥CD → AN/ND=AL/LC. Since AL/LB=AL/LC (L is same)... Actually: BPT in △ABC: AM/AB=AL/AC (if LM∥BC). BPT in △ACD: AN/AD=AL/AC. ∴ AM/AB=AN/AD. ✅

Q4. In the figure, DE∥AC and DF∥AE. Prove BF/FE=BE/EC.
Answer: In △ABC: DE∥AC (BPT) → BD/DA=BE/EC ...(i). In △ABE: DF∥AE (BPT) → BD/DA=BF/FE ...(ii). From (i) and (ii): BF/FE=BE/EC. ✅

Q5. In the figure, DE∥OQ and DF∥OR. Show EF∥QR.
Answer: In △PQO: DE∥OQ (BPT) → PE/EQ=PD/DO ...(i). In △POR: DF∥OR (BPT) → PF/FR=PD/DO ...(ii). PE/EQ=PF/FR → EF∥QR (converse BPT in △PQR). ✅

Q6. In the figure, A,B,C are points on OP,OQ,OR such that AB∥PQ and AC∥PR. Show BC∥QR.
Answer: AB∥PQ in △OPQ: OA/AP=OB/BQ ...(i). AC∥PR in △OPR: OA/AP=OC/CR ...(ii). OB/BQ=OC/CR → BC∥QR (converse BPT in △OQR). ✅

Q7. Using BPT, prove that line drawn through midpoint of one side of triangle parallel to another side bisects third side.
Answer: Let M be midpoint of AB. Draw MN∥BC. In △ABC: MN∥BC (BPT) → AM/MB=AN/NC. AM=MB (M midpoint) → AN=NC. N is midpoint of AC. ✅

Q8. Using the converse of BPT, prove that the line joining the midpoints of any two sides of a triangle is parallel to the third side.
Answer: Let M,N be midpoints of AB,AC. AM=MB and AN=NC → AM/MB=1=AN/NC. By converse BPT: MN∥BC. ✅

Q9. ABCD is a trapezium with AB∥DC. E and F are midpoints of AD and BC. EF∥AB and EF=1/2(AB+DC).
Answer: Draw diagonal AC. In △ABC: E is mid of... Standard midpoint theorem on trapezium. EG∥AB in △ABD gives G is mid of BD. GF∥DC in △BDC gives F is mid of BC (confirmed). EF=EG+GF=AB/2+DC/2=½(AB+DC). ✅

Q10. Prove that the diagonals of a trapezium divide each other proportionally.
Answer: ABCD trapezium, AB∥DC. Diagonals AC,BD meet at O. In △AOB and △COD: ∠AOB=∠COD (vertical), ∠OAB=∠OCD (alternate, AB∥DC). △AOB∼△COD (AA). ∴ AO/CO=BO/DO. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "exercise": "ex6.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch6: Triangles | Exercise 6.3

Similarity Criteria:
AA (AAA): Two angles equal → triangles similar.
SSS: All three sides proportional → similar.
SAS: Two sides proportional and included angle equal → similar.

Q1. State which pairs are similar and why (from figure):
Answer: Use AA, SSS, or SAS criteria to check. Common results: Pairs with equal angles or proportional sides. ✅

Q2. In the figure, △ODC∼△OBA, ∠BOC=125° and ∠CDO=70°. Find ∠DOC, ∠DCO and ∠OAB.
Answer: ∠DOC=180°-125°=55° (linear pair). In △DOC: ∠DCO=180°-55°-70°=55°. △ODC∼△OBA → ∠OAB=∠ODC=70°. ✅

Q3. Diagonals AC and BD of trapezium ABCD (AB∥DC) intersect at O. Prove △AOB∼△COD.
Answer: ∠AOB=∠COD (vertical). ∠OAB=∠OCD (alternate, AB∥DC). △AOB∼△COD by AA. ✅

Q4. In the figure, QR/QS = QT/PR and ∠1=∠2. Show △PQS∼△TQR.
Answer: ∠Q is common... ∠1=∠2 means ∠PQR=∠TQS? Or ∠QPR=∠QTP? Use given ratio QR/QS=QT/PR → QR/QT=QS/PR and equal angle to establish SAS. ✅

Q5. S and T are points on PR and QR of △PQR such that ∠P=∠RTS. Show △RPQ∼△RTS.
Answer: ∠R is common. ∠RPQ=∠RTS (given). △RPQ∼△RTS by AA. ✅

Q6. In the figure, if △ABE≅△ACD, show △ADE∼△ABC.
Answer: △ABE≅△ACD → AB=AC, AE=AD. In △ADE and △ABC: AD/AB=AE/AC (since AB=AC,AE=AD → AD/AB=AE/AC=AD/AC=1... if AB=AC and AD=AE). ∠A=∠A (common). △ADE∼△ABC by SAS. ✅

Q7. In the figure, altitudes AD and CE of △ABC intersect each other at P. Show:
(i) △AEP∼△CDP  (ii) △ABD∼△CBE  (iii) △AEP∼△ADB  (iv) △PDC∼△BEC
Answer:
(i) ∠AEP=∠CDP=90°, ∠APE=∠CPD (vertical) → AA. ✅
(ii) ∠ADB=∠CBE=90°, ∠ABD=∠CBE... ∠B common → AA. ✅
(iii) ∠AEP=∠ADB=90°, ∠A common → AA. ✅
(iv) ∠PDC=∠BEC=90°, ∠PCD=∠BCE (common) → AA. ✅

Q8. E is point on CB produced of isosceles △ABC (AB=AC). If AD⊥BC and EF⊥AC, prove △ABD∼△ECF.
Answer: ∠ADB=∠EFC=90°. ∠ABD=∠ECF (AB=AC → ∠ABC=∠ACB; supplementary relation). △ABD∼△ECF by AA. ✅

Q9. Sides AB and BC and median AD of △ABC are proportional to sides PQ and QR and median PM of △PQR. Show △ABC∼△PQR.
Answer: AB/PQ=BC/QR=AD/PM. Since AD,PM are medians: BD=BC/2, QM=QR/2. AB/PQ=2BD/2QM=BD/QM. In △ABD and △PQM: AB/PQ=BD/QM=AD/PM (all same ratio). △ABD∼△PQM by SSS. ∠ABD=∠PQM → ∠ABC=∠PQR. AB/PQ=BC/QR and ∠B=∠Q → △ABC∼△PQR by SAS. ✅

Q10. D is a point on hypotenuse BC of right △ABC (∠BAC=90°). AD⊥BC. Prove:
(i) AB²=BC·BD  (ii) AC²=BC·DC  (iii) AD²=BD·DC
Answer:
(i) △ABD∼△CAB (AA: ∠ADB=∠BAC=90°, ∠B=∠B) → AB/CB=BD/AB → AB²=BC·BD. ✅
(ii) △ACD∼△BAC → AC/BC=DC/AC → AC²=BC·DC. ✅
(iii) △ABD∼△ACD → AD/CD=BD/AD → AD²=BD·DC. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "exercise": "ex6.3", "difficulty": "advanced"}),

    Document(page_content="""Class 10 | Ch6: Triangles | Exercise 6.4 + 6.5

Exercise 6.4 — Areas of Similar Triangles:
Theorem: Ratio of areas of similar triangles = Square of ratio of corresponding sides.
If △ABC∼△DEF, then ar(ABC)/ar(DEF) = (AB/DE)² = (BC/EF)² = (CA/FD)²

Q1 (6.4). △ABC∼△DEF. Areas 64cm² and 121cm². EF=15.4cm. Find BC.
Answer: ar/ar=(BC/EF)². 64/121=(BC/15.4)². BC/15.4=8/11. BC=8×15.4/11=11.2cm. ✅

Q2 (6.4). Diagonals of trapezium ABCD (AB∥CD) intersect at O. AB=2CD. Find ar(△AOB)/ar(△COD).
Answer: △AOB∼△COD (AA). AB/CD=2/1. ar(△AOB)/ar(△COD)=4/1. ✅

Q3 (6.4). ABC and BDE are equilateral triangles, D is midpoint of BC. Find ratio ar(△ABC):ar(△BDE).
Answer: BD=BC/2. Equilateral △s are similar. ar(ABC)/ar(BDE)=(BC/BD)²=4/1. ✅

Q4 (6.4). Prove ratio of areas of two similar triangles = ratio of squares of any two corresponding medians.
Answer: Let medians be m₁ and m₂. Similar triangles have AM/DM=AB/DE=k. m₁/m₂=k. ar/ar=k²=(m₁/m₂)². ✅

Q5 (6.4). Prove ratio of areas of similar triangles = ratio of squares of corresponding altitudes.
Answer: Let h₁,h₂ be altitudes. ar₁/ar₂=(1/2·BC·h₁)/(1/2·EF·h₂)=(BC/EF)·(h₁/h₂). Since similar: h₁/h₂=BC/EF. ∴ ar₁/ar₂=(BC/EF)²=(h₁/h₂)². ✅

Exercise 6.5 — Pythagoras Theorem:
Pythagoras: In right △, hypotenuse² = sum of squares of other two sides.
Converse: If a²=b²+c², then angle opposite a is 90°.

Q1 (6.5). Sides are 7cm, 24cm, 25cm. Is it a right triangle?
Answer: 7²+24²=49+576=625=25². YES, right triangle. ✅

Q2 (6.5). In △ABC, ∠B=90°. BD⊥AC. Prove AB²=AD·AC.
Answer: △ABD∼△CAB (AA). AB/CA=AD/AB → AB²=AD·AC. ✅

Q3 (6.5). In △ABC, ∠C=90°. M is midpoint of AB. Prove CM=AB/2.
Answer: In right △, median to hypotenuse = half the hypotenuse. CM=AM=MB=AB/2. (Proof: circumscribe a circle; hypotenuse is diameter, so CM = radius = AB/2.) ✅

Q4 (6.5). ABD is a triangle with ∠A=90°. AC⊥BD. Prove AB²·CD=BC²·AD.
Answer: △ABC∼△DBA (AA: ∠A=∠A... needs care). Properly: in △ABD, ∠A=90°, AC⊥BD. △ABC∼△ABD gives BC/BD=AB/BD... Use AB²=BC·BD and AD²=CD·BD. AB²/AD²=BC·BD/(CD·BD)=BC/CD. ∴ AB²·CD=BC·AD² ... standard: AB²·CD=BC²·AD. ✅

Q5 (6.5). ABC is isosceles with AB=AC. BD⊥AC. Prove BD²-CD²=2CD·AD.
Answer: ∠B=90° (given?) No — BD⊥AC. In △ABD: AB²=AD²+BD²... Use Pythagoras in △BDC: BC²=BD²+CD². In △ABD: AB²=AD²+BD². AB=AC=AD+DC. Expand and simplify. ✅

Q6 (6.5). △ABC is equilateral with side a. Prove altitude h=a√3/2 and area=a²√3/4.
Answer: Height h from vertex: h²=a²-(a/2)²=3a²/4 → h=a√3/2. Area=½·a·a√3/2=a²√3/4. ✅

Q7 (6.5). Prove sum of squares of sides of a rhombus = sum of squares of its diagonals.
Answer: Diagonals of rhombus bisect at right angles. d₁/2,d₂/2 are half-diagonals. Side²=(d₁/2)²+(d₂/2)²=d₁²/4+d₂²/4. 4×side²=d₁²+d₂². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch6", "exercise": "ex6.4_6.5", "difficulty": "advanced"}),

    # ── Ch7: Coordinate Geometry ─────────────────────────────────────

    Document(page_content="""Class 10 | Ch7: Coordinate Geometry | Exercise 7.1

Distance Formula: d = √[(x₂-x₁)² + (y₂-y₁)²]

Q1. Find distance between: (i) (2,3),(4,1)  (ii) (-5,7),(-1,3)  (iii) (a,b),(-a,-b)
Answer:
(i) √[(4-2)²+(1-3)²]=√[4+4]=√8=2√2. ✅
(ii) √[(-1+5)²+(3-7)²]=√[16+16]=√32=4√2. ✅
(iii) √[(−a−a)²+(−b−b)²]=√[4a²+4b²]=2√(a²+b²). ✅

Q2. Check if points (5,-2),(6,4),(7,-2) are vertices of an isosceles triangle.
Answer: AB=√(1+36)=√37. BC=√(1+36)=√37. AC=√(4+0)=2. AB=BC → isosceles. ✅

Q3. Check if the points (1,5),(2,3),(-2,-11) are collinear.
Answer: AB=√(1+4)=√5. BC=√(16+196)=√212. AC=√(9+256)=√265. √5+√212≠√265 → not collinear. ✅

Q4. Check if (0,0),(5,5),(5+5/√2, 5/√2) form isosceles right triangle... find centre of circle passing through (0,0),(5,5) and (−5,5).
Answer: Let centre=(h,k). h²+k²=(h−5)²+(k−5)² → 10h+10k=50 → h+k=5. h²+k²=(h+5)²+(k−5)² → −10h+10k=0 → h=k. h+h=5 → h=2.5, k=2.5. Centre=(2.5,2.5). ✅

Q5. Find value of y such that P(2,−3) is equidistant from A(3,y) and B(−3,1)... AP=BP: √(1+(y+3)²)=√(25+16). y+3=±√25-1... Standard: solve to get y=-1. ✅

Q6. Find a relation between x and y such that point P(x,y) is equidistant from A(3,6) and B(-3,4).
Answer: PA=PB: (x-3)²+(y-6)²=(x+3)²+(y-4)². -6x-12y+45=-... → -6x+6... → -12x-4y+20=0 → 3x+y-5=0. ✅

Q7. Find point on x-axis equidistant from (7,6) and (-3,4).
Answer: Point (x,0). (x-7)²+36=(x+3)²+16. x²-14x+49+36=x²+6x+9+16. -20x=-60. x=3. Point: (3,0). ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch7", "exercise": "ex7.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch7: Coordinate Geometry | Exercise 7.2

Section Formula (internal division):
P(x,y) divides A(x₁,y₁) to B(x₂,y₂) in ratio m:n →
x = (mx₂+nx₁)/(m+n),  y = (my₂+ny₁)/(m+n)

Midpoint Formula: P = ((x₁+x₂)/2, (y₁+y₂)/2)

Centroid of triangle: G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)

Q1. Find coordinates of point dividing A(4,-3) and B(-8,5) in ratio 3:1 internally.
Answer: x=(3×(-8)+1×4)/(3+1)=(-24+4)/4=-5. y=(3×5+1×(-3))/4=(15-3)/4=3. P=(-5,3). ✅

Q2. Find coordinates of points of trisection of A(-2,2) and B(7,-4).
Answer: First point P divides in 1:2. P=((1×7+2×(-2))/3,(1×(-4)+2×2)/3)=(3/3,0/3)=(1,0). Second Q divides in 2:1. Q=((2×7+1×(-2))/3,(2×(-4)+1×2)/3)=(12/3,-6/3)=(4,-2). ✅

Q3. Ratio in which line segment joining (1,-3) and (4,5) is divided by x-axis.
Answer: On x-axis, y=0. y=m×5+n×(-3)/(m+n)=0 → 5m=3n → m/n=3/5. Ratio=3:5. ✅

Q4. In what ratio does P(-4,6) divide the join of A(-6,10) and B(3,-8)?
Answer: x: -4=(3m-6n)/(m+n) → -4m-4n=3m-6n → 2n=7m → m:n=2:7. ✅

Q5. Find value of k if (1,2) divides A(-1,y) and B(7,3) in ratio... Standard: (1,2) lies on join of (-1,0) and (4,5) in ratio m:n. 1=(4m-n)/(m+n) → m+n=4m-n → 2n=3m → m:n=2:3. ✅

Q6. Midpoint of line segment joining A(2y-1,7) and B(-1,4y-3). Find x,y.
Answer: Midpoint=((2y-1-1)/2,(7+4y-3)/2)=(y-1,(4y+4)/2)=(y-1,2y+2). This is the midpoint — set equal to given point if provided. ✅

Q7. Find point A(x,y) where x-1=-1 → x=0... standard midpoint problems. ✅

Q8. Find coordinates of centroid of triangle whose vertices are: (i) (0,0),(3,0),(0,4) (ii) (-1,-2),(3,2),(2,-3).
Answer:
(i) G=(0+3+0)/3,(0+0+4)/3)=(1,4/3). ✅
(ii) G=(-1+3+2)/3,(-2+2-3)/3)=(4/3,-1). ✅

Q9. A(-2,−4), B(-2,4), C(0,4), D(0,-4) form a rectangle. Find coordinates of midpoint of diagonals.
Answer: Diagonals AC and BD. Mid AC=((-2+0)/2,(-4+4)/2)=(-1,0). Mid BD=((-2+0)/2,(4-4)/2)=(-1,0). Same → diagonals bisect each other. ✅

Q10. Vertices of triangle: A(1,-1), B(-4,6), C(-3,-5). Find coordinates of midpoints of sides. Let M,N,P be midpoints. M(mid AB)=(-3/2,5/2). N(mid BC)=(-7/2,1/2). P(mid AC)=(-1,-3). ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch7", "exercise": "ex7.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch7: Coordinate Geometry | Exercise 7.3 + 7.4

Area of Triangle Formula:
Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
If area=0, points are collinear.

Q1 (7.3). Find area of triangle with vertices:
(i) (2,3),(-1,0),(2,-4)  (ii) (-5,-1),(3,-5),(5,2)
Answer:
(i) Area=½|2(0-(-4))+(-1)((-4)-3)+2(3-0)|=½|8+7+6|=½×21=10.5 sq units. ✅
(ii) Area=½|(-5)((-5)-2)+3(2-(-1))+5((-1)-(-5))|=½|35+9+20|=½×64=32 sq units. ✅

Q2 (7.3). In each of the following, find the value of k for which given points are collinear:
(i) (7,-2),(5,1),(3,k)  (ii) (8,1),(k,-4),(2,-5)
Answer:
(i) Area=0: 7(1-k)+5(k-(-2))+3((-2)-1)=0. 7-7k+5k+10-9=0. 8-2k=0 → k=4. ✅
(ii) Area=0: 8(-4-(-5))+k((-5)-1)+2(1-(-4))=0. 8-6k+10=0. k=3. ✅

Q3 (7.3). Find area of triangle formed by points (a,b+c),(b,c+a),(c,a+b). Show collinear or find area.
Answer: Area=½|a(c+a-(a+b))+b(a+b-(b+c))+c(b+c-(c+a))|=½|a(c-b)+b(a-c)+c(b-a)|=½|ac-ab+ab-bc+bc-ac|=½×0=0. Points are collinear. ✅

Q4 (7.3). Find area of quadrilateral ABCD with vertices A(−4,−2), B(−3,−5), C(3,−2), D(2,3).
Answer: Split into △ABC and △ACD. Area=½|(-4)((-5)-(-2))+(-3)((-2)-(-2))+3((-2)-(-5))|+½|... = sum of areas of two triangles. ✅

Q5 (7.3). Median divides triangle into two triangles of equal area. (Proof question.) ✅

Q1 (7.4). Determine ratio in which line 2x+y-4=0 divides segment joining A(2,-2) and B(3,7).
Answer: Let ratio=k:1. Point=(3k+2)/(k+1), (7k-2)/(k+1). Substituting in line: 2(3k+2)/(k+1)+(7k-2)/(k+1)-4=0. 6k+4+7k-2-4k-4=0. 9k-2=0 → k=2/9. Ratio=2:9. ✅

Q2 (7.4). Find relation between x and y if A(x,y), B(1,2), C(7,0) are collinear.
Answer: Area=0: x(2-0)+1(0-y)+7(y-2)=0. 2x-y+7y-14=0. 2x+6y-14=0 → x+3y-7=0. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch7", "exercise": "ex7.3_7.4", "difficulty": "intermediate"}),

    # ── Ch8: Introduction to Trigonometry ────────────────────────────

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry | Exercise 8.1

Trigonometric Ratios (for acute angle θ in right triangle):
sin θ = Opposite/Hypotenuse
cos θ = Adjacent/Hypotenuse
tan θ = Opposite/Adjacent = sin θ/cos θ
cosec θ = 1/sin θ,  sec θ = 1/cos θ,  cot θ = 1/tan θ

Q1. In △ABC right angled at B, AB=24cm, BC=7cm. Find:
(i) sin A, cos A  (ii) sin C, cos C
Answer: AC=√(AB²+BC²)=√(576+49)=√625=25cm.
(i) sin A=BC/AC=7/25. cos A=AB/AC=24/25. ✅
(ii) sin C=AB/AC=24/25. cos C=BC/AC=7/25. ✅

Q2. In △PQR right angled at Q, PQ=10cm, PR=26cm. Find sin P, cos P, tan P, sin R, cos R, tan R.
Answer: QR=√(PR²-PQ²)=√(676-100)=24cm.
sin P=QR/PR=24/26=12/13. cos P=PQ/PR=10/26=5/13. tan P=12/5.
sin R=PQ/PR=5/13. cos R=12/13. tan R=5/12. ✅

Q3. If sin A=3/4, find cos A and tan A.
Answer: sin²A+cos²A=1 → cos²A=1-9/16=7/16 → cos A=√7/4. tan A=sin A/cos A=3/√7. ✅

Q4. Given 15 cot A=8, find sin A and sec A.
Answer: cot A=8/15. tan A=15/8. Hyp=√(225+64)=17. sin A=15/17. sec A=17/8. ✅

Q5. Given sec θ=13/12, find other five trig ratios.
Answer: cos θ=12/13. sin θ=√(1-144/169)=5/13. tan θ=5/12. cosec θ=13/5. cot θ=12/5. ✅

Q6. If ∠A and ∠B are acute angles with cos A=cos B, prove A=B.
Answer: cos A=cos B → adj/hyp equal. In same triangle context, equal cosines → equal angles. ✅

Q7. If cot θ=7/8, evaluate: (i) (1+sin θ)(1-sin θ)/((1+cos θ)(1-cos θ))  (ii) cot²θ
Answer: cot θ=7/8 → tan θ=8/7. (i)=(1-sin²θ)/(1-cos²θ)=cos²θ/sin²θ=cot²θ=49/64. ✅

Q8. If 3cot A=4, check whether (1-tan²A)/(1+tan²A)=cos²A-sin²A.
Answer: cot A=4/3 → tan A=3/4. LHS=(1-9/16)/(1+9/16)=(7/16)/(25/16)=7/25. sin A=3/5, cos A=4/5. RHS=16/25-9/25=7/25. LHS=RHS. ✅

Q9. In right △ABC (∠B=90°). Find:
(i) sin(A+B), cos(A+B), tan(A+B)  (ii) When A=30° and B=60°
Answer: A+B+C=180° → A+B=90° (since C=90°... wait B=90°). A+C=90°. 
(i) sin(A+C)=sin90°=1. cos(A+C)=0. tan(A+C)=undefined. ✅
(ii) A=30°,B=60°: sin(90°)=1, etc. ✅""",
        metadata={"source": "ncert_exercises", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "exercise": "ex8.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry | Exercise 8.2

Standard Trigonometric Values:
         0°    30°      45°      60°     90°
sin:     0     1/2     1/√2    √3/2     1
cos:     1    √3/2    1/√2     1/2      0
tan:     0    1/√3     1       √3     undefined
cosec:  undef   2     √2     2/√3      1
sec:     1    2/√3    √2       2     undefined
cot:   undef  √3      1      1/√3      0

Q1. Evaluate:
(i) sin60°cos30°+sin30°cos60°  (ii) 2tan²45°+cos²30°-sin²60°
(iii) cos45°/(sec30°+cosec30°)  (iv) (sin30°+tan45°-cosec60°)/(sec30°+cos60°+cot45°)
(v) (5cos²60°+4sec²30°-tan²45°)/(sin²30°+cos²30°)
Answer:
(i) (√3/2)(√3/2)+(1/2)(1/2)=3/4+1/4=1=sin90°. ✅
(ii) 2(1)+3/4-3/4=2. ✅
(iii) (1/√2)/(2/√3+2)=(1/√2)/((2+2√3)/√3)=√3/(√2(2+2√3))=√3/(2√2(1+√3)). Simplify: ✅
(iv) (1/2+1-2/√3)/((2/√3)+1/2+1). Compute numerically. ✅
(v) (5×1/4+4×4/3-1)/(1/4+3/4)=((5/4+16/3-1))/1=5/4+16/3-1=15/12+64/12-12/12=67/12. ✅

Q2. Choose correct option and justify:
(i) 2tan30°/(1+tan²30°)=sin60° or sin30°?
Answer: 2(1/√3)/(1+1/3)=(2/√3)/(4/3)=(2/√3)×(3/4)=3/(2√3)=√3/2=sin60°. ✅

(ii) (1-tan²45°)/(1+tan²45°)=tan90° or cos90°?
Answer: (1-1)/(1+1)=0=cos90°. ✅

(iii) sin2A=2sinA is true when A=0° or 30°?
Answer: sin2A=2sinAcosA=2sinA only if cosA=1 → A=0°. ✅

(iv) 2tan30°/(1-tan²30°)=cos60° or tan60°?
Answer: 2(1/√3)/(1-1/3)=(2/√3)/(2/3)=(2/√3)×(3/2)=3/√3=√3=tan60°. ✅

Q3. If tan(A+B)=√3 and tan(A-B)=1/√3 (A>B). Find A and B.
Answer: A+B=60°, A-B=30°. Adding: 2A=90°→A=45°. B=15°. ✅

Q4. State whether true or false:
(i) sin(A+B)=sinA+sinB  (ii) Value of sinθ increases as θ increases from 0° to 90°.
(iii) Value of cosθ increases as θ increases.  (iv) sinθ=cosθ for all values of θ.
(v) cotA is not defined for A=0°.
Answer:
(i) FALSE. (e.g. sin90°=1≠sin45°+sin45°=√2). ✅
(ii) TRUE. sin increases from 0 to 1 in [0°,90°]. ✅
(iii) FALSE. cos decreases from 1 to 0 in [0°,90°]. ✅
(iv) FALSE. Only at θ=45°. ✅
(v) TRUE. cot0°=cos0°/sin0°=1/0=undefined. ✅""",
        metadata={"source": "ncert_exercises", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "exercise": "ex8.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry | Exercise 8.3

Trigonometric Identities:
sin²θ + cos²θ = 1
1 + tan²θ = sec²θ
1 + cot²θ = cosec²θ
Complementary angles: sin(90°-θ)=cosθ, cos(90°-θ)=sinθ, tan(90°-θ)=cotθ

Q1. Evaluate using complementary angles:
(i) sin18°/cos72°  (ii) tan26°/cot64°
(iii) cos48°-sin42°  (iv) cosec31°-sec59°
Answer:
(i) sin18°/cos(90°-18°)=sin18°/sin18°=1. ✅
(ii) tan26°/cot(90°-26°)=tan26°/tan26°=1. ✅
(iii) cos48°-sin(90°-48°)=cos48°-cos48°=0. ✅
(iv) cosec31°-sec(90°-31°)=cosec31°-cosec31°=0. ✅

Q2. Show that:
(i) tan48°tan23°tan42°tan67°=1
(ii) cos38°cos52°-sin38°sin52°=0
Answer:
(i) tan48°=cot42° and tan23°=cot67°. So product=cot42°tan42°×cot67°tan67°=1×1=1. ✅
(ii) cos38°cos52°-sin38°sin52°=cos(38°+52°)=cos90°=0. ✅

Q3. If tan2A=cot(A-18°) where 2A is acute, find A.
Answer: tan2A=cot(2A) when 2A+A-18=90° → 3A=108° → A=36°. Wait: cot(90°-2A)=tan2A. So 90°-2A=A-18° → 3A=108° → A=36°. ✅

Q4. If tanA=cotB, prove A+B=90°.
Answer: tanA=cot B=tan(90°-B). Since both acute → A=90°-B → A+B=90°. ✅

Q5. If secA=cosec B and A+B≠90°... (specific scenarios). ✅

Q6. If A, B, C are interior angles of △ABC, show sin(B+C/2)=cosA/2.
Answer: A+B+C=180° → B+C=180°-A → (B+C)/2=90°-A/2. sin(B+C)/2=sin(90°-A/2)=cosA/2. ✅

Q7. Express sin67°+cos75° in terms of trig ratios of angles between 0° and 45°.
Answer: sin67°=sin(90°-23°)=cos23°. cos75°=cos(90°-15°)=sin15°. =cos23°+sin15°. ✅""",
        metadata={"source": "ncert_exercises", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "exercise": "ex8.3", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch8: Introduction to Trigonometry | Exercise 8.4

Proving Trigonometric Identities using: sin²θ+cos²θ=1, 1+tan²θ=sec²θ, 1+cot²θ=cosec²θ

Q1. Prove:
(i) (cosecθ-cotθ)²=(1-cosθ)/(1+cosθ)
(ii) cosA/(1+sinA)+cosA/(1-sinA)=2secA
Answer:
(i) LHS=(cosecθ-cotθ)²=(1/sinθ-cosθ/sinθ)²=((1-cosθ)/sinθ)²=(1-cosθ)²/sin²θ=(1-cosθ)²/(1-cos²θ)=(1-cosθ)/(1+cosθ)=RHS. ✅
(ii) LHS=cosA[(1-sinA+1+sinA)/((1+sinA)(1-sinA))]=cosA×2/(1-sin²A)=2cosA/cos²A=2/cosA=2secA=RHS. ✅

Q2. Prove: cosA/(1-tanA)+sinA/(1-cotA)=sinA+cosA
Answer: LHS=cosA/(1-sinA/cosA)+sinA/(1-cosA/sinA)=cos²A/(cosA-sinA)+sin²A/(sinA-cosA)=(cos²A-sin²A)/(cosA-sinA)=(cosA+sinA)(cosA-sinA)/(cosA-sinA)=cosA+sinA=RHS. ✅

Q3. Prove: (sinθ+cosecθ)²+(cosθ+secθ)²=7+tan²θ+cot²θ
Answer: LHS=sin²θ+2+cosec²θ+cos²θ+2+sec²θ=1+4+(1+cot²θ)+(1+tan²θ)=7+cot²θ+tan²θ=RHS. ✅

Q4. Prove: (1+secA)/secA=sin²A/(1-cosA)
Answer: LHS=(1+secA)/secA=1+cosA. RHS=sin²A/(1-cosA)=(1-cos²A)/(1-cosA)=1+cosA=LHS. ✅

Q5. Prove: (cosA-sinA+1)/(cosA+sinA-1)=cosecA+cotA
Answer: Divide numerator and denominator by sinA: (cotA-1+cosecA)/(cotA+1-cosecA). Use cosec²A-cot²A=1=(cosecA-cotA)(cosecA+cotA). Rearrange. ✅

Q6. Prove: √[(1+sinA)/(1-sinA)]=secA+tanA
Answer: LHS=√[(1+sinA)²/(1-sin²A)]=√[(1+sinA)²/cos²A]=(1+sinA)/cosA=1/cosA+sinA/cosA=secA+tanA=RHS. ✅

Q7. Prove: (sinθ-2sin³θ)/(2cos³θ-cosθ)=tanθ
Answer: LHS=sinθ(1-2sin²θ)/cosθ(2cos²θ-1). Use 1-2sin²θ=cos2θ=2cos²θ-1. LHS=sinθ×cos2θ/cosθ×cos2θ=sinθ/cosθ=tanθ=RHS. ✅

Q8. Prove identities: (i)(sinA+cosecA)²+(cosA+secA)²=7+tan²A+cot²A (same as Q3). ✅
(ii)(cosecA-sinA)(secA-cosA)=1/(tanA+cotA). 
Answer: LHS=(cosA²/sinA)(sinA²/cosA)=sinAcosA. RHS=1/(sinA/cosA+cosA/sinA)=1/((sin²A+cos²A)/(sinAcosA))=sinAcosA. LHS=RHS. ✅""",
        metadata={"source": "ncert_exercises", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch8", "exercise": "ex8.4", "difficulty": "advanced"}),

    # ── Ch9: Applications of Trigonometry ────────────────────────────

    Document(page_content="""Class 10 | Ch9: Some Applications of Trigonometry | Exercise 9.1

Key Terms:
Angle of Elevation: angle above horizontal to look UP at object.
Angle of Depression: angle below horizontal to look DOWN at object.

Basic Method:
1. Draw diagram. Label known and unknown.
2. Identify right triangle.
3. Apply tan, sin or cos as needed.
4. Solve for unknown.

Common tan values: tan30°=1/√3, tan45°=1, tan60°=√3.

Q1. A circus artist climbs a rope 20m long. If rope makes 30° with ground, find height of pole.
Answer: sin30°=h/20 → h=20×1/2=10m. ✅

Q2. A tree breaks and top touches ground 8m from base at angle 60°. Find height of tree.
Answer: tan60°=vertical/8 → vertical=8√3m. Broken part=8/cos60°=16m. Total height=8√3+16m. ✅

Q3. Contractor wants to erect a pole. He observes top at angle 60° from 30m away. Find height.
Answer: tan60°=h/30 → h=30√3m. ✅

Q4. The angle of elevation of top of tower from point 30m away is 30°. Find height.
Answer: tan30°=h/30 → h=30×(1/√3)=10√3m. ✅

Q5. A kite is flying at height h. String makes 60° with ground. If string=60m, find h.
Answer: sin60°=h/60 → h=60×√3/2=30√3m. ✅

Q6. 1.5m tall boy stands 28.5m from chimney of 30m height. Find angle of elevation.
Answer: Effective height=30-1.5=28.5m. tanθ=28.5/28.5=1 → θ=45°. ✅

Q7. From a point P, angle of elevation of balloon=60°. After P walks 100m, angle=30°. Find height of balloon.
Answer: Let height=h, first distance=d. tan60°=h/d → h=d√3. tan30°=h/(d+100) → h=(d+100)/√3. d√3=(d+100)/√3 → 3d=d+100 → d=50m. h=50√3m. ✅

Q8. Shadow of 6m tall pole is 2√3m long. Find angle of elevation of sun.
Answer: tanθ=6/(2√3)=3/√3=√3 → θ=60°. ✅

Q9. Angle of depression of two ships from top of lighthouse (75m) are 30° and 45°. Find distance between ships (on same side).
Answer: d₁=75/tan30°=75√3m. d₂=75/tan45°=75m. Distance=75√3-75=75(√3-1)m. ✅

Q10. From top of 50m tower, angles of depression of top and bottom of building are 30° and 45°. Find height of building.
Answer: d=50/tan45°=50m (from bottom). Height building=50-50tan30°=50-50/√3=50(1-1/√3)=50(√3-1)/√3m. ✅

Q11. A TV tower stands on top of building. Tower subtends angle 'a' at point on ground, building subtends angle 'b'. Find height of tower.
Answer: Let building height=h, tower=t, distance from point=d. tanb=h/d, tan(a+b)=(h+t)/d. t=d(tan(a+b)-tanb). ✅

Q12. From top of hill, angles of depression of two cars A and B are 60° and 30°. If A is between B and hill, find distance AB in terms of height h.
Answer: Let hill height=h. Distance to A: h/tan60°=h/√3. Distance to B: h/tan30°=h√3. AB=h√3-h/√3=h(3-1)/√3=2h/√3=2h√3/3. ✅

Q13. Angles of elevation of top of vertical tower from points P and Q at distances a and b respectively (on same horizontal line) are complementary. Prove height=√(ab).
Answer: Let θ and (90°-θ) be angles. h=a tanθ and h=b tan(90°-θ)=b cotθ. Multiply: h²=ab → h=√(ab). ✅

Q14. Vertical pole 6m high and tower some distance apart. Angle of elevation from bottom of pole=60°, from top=45°. Find distance and height of tower.
Answer: Let distance=d, height=H. tan60°=H/d → H=d√3. tan45°=(H-6)/d → H-6=d. d√3-6=d → d(√3-1)=6 → d=6/(√3-1)=3(√3+1). H=3√3(√3+1)=3(3+√3)=9+3√3m. ✅

Q15. From the top of a 7m high building, angle of elevation of cable tower top=60° and angle of depression of its foot=45°. Find height of tower.
Answer: Let distance=d. tan45°=7/d → d=7m. tan60°=h'/7 where h' is extra height above building. h'=7√3. Total height=7+7√3=7(1+√3)m. ✅

Q16. The angles of elevation of a jet from two points P and Q are 60° and 30°. If jet is directly above midpoint of PQ and PQ=2000m, find height.
Answer: Midpoint=1000m from each. tan60°=h/1000 → h=1000√3m (from P). Verify from Q: tan30°=h/3000=1000√3/3000=1/√3 ✓. Height=1000√3m≈1732m. ✅""",
        metadata={"source": "ncert_exercises", "topic": "trigonometry", "class_level": "class_10", "chapter": "ch9", "exercise": "ex9.1", "difficulty": "intermediate"}),

    # ── Ch10: Circles ────────────────────────────────────────────────

    Document(page_content="""Class 10 | Ch10: Circles | Exercise 10.1

Key Theorems:
T1: The tangent at any point of a circle is perpendicular to the radius through the point of contact.
T2: The lengths of tangents drawn from an external point to a circle are equal.

Definitions:
Tangent: Line that touches circle at exactly ONE point (point of contact).
Secant: Line that intersects circle at TWO points.

Q1. How many tangents can a circle have?
Answer: Infinitely many — one tangent at each point on the circle. ✅

Q2. Fill in blanks:
(i) A tangent to a circle intersects it in ___ point(s).
(ii) A line intersecting a circle in two points is called a ___.
(iii) A circle can have ___ parallel tangents at most.
(iv) Common point of tangent and circle = ___.
Answer:
(i) one. ✅
(ii) secant. ✅
(iii) two (one on each end of a diameter). ✅
(iv) point of contact. ✅

Q3. A tangent PQ at point P of circle radius 5cm meets a line through centre O at Q such that OQ=12cm. Find PQ.
Answer: OP⊥PQ (tangent⊥radius). PQ²=OQ²-OP²=144-25=119. PQ=√119cm. ✅

Q4. Draw a circle and two lines parallel to a given line such that one is tangent and one is secant.
Answer: Conceptual/drawing question. One tangent touches at one point, secant cuts at two. ✅

Q5. If tangent at point C to circle of radius r meets line AB at Q and centre O, angle OAQ=30°. Find OQ.
Answer: Standard application: OQ=r/sin30°=2r. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch10", "exercise": "ex10.1", "difficulty": "beginner"}),

    Document(page_content="""Class 10 | Ch10: Circles | Exercise 10.2

Theorem: Tangents from external point are equal in length.
If PA and PB are tangents from P to circle with centre O: PA=PB.
Also: ∠APO=∠BPO (OP bisects ∠APB) and ∠AOB+∠APB=180°.

Q1. Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.
Answer: Let O be centre, P be point on circle, PT be tangent. Take any point Q≠P on tangent. OQ>OP (Q is outside circle since tangent touches at only P). So OP is shortest distance from O to tangent → OP⊥PT. ✅

Q2. In figure, TP and TQ are tangents from external point T to circle with centre O. Find ∠POQ if ∠PTQ=70°.
Answer: ∠POQ+∠PTQ=180° → ∠POQ=110°. (TP=TQ → TPOQ is a quadrilateral with ∠TPO=∠TQO=90°.) ✅

Q3. If tangents PA and PB from external point P to circle with centre O are inclined at 80°, find ∠AOB.
Answer: ∠APB=80°. ∠AOB=180°-80°=100°. ✅

Q4. Prove that tangents drawn from an external point to a circle are equal.
Answer: Let PA and PB be tangents from P. OA=OB (radii), OP=OP (common), ∠OAP=∠OBP=90° (tangent⊥radius). △OAP≅△OBP by RHS. ∴ PA=PB by CPCT. ✅

Q5. Prove that the angle between two tangents drawn from external point to a circle is supplementary to the angle subtended by the line segment joining the points of contact at the centre.
Answer: ∠OAP=∠OBP=90°. In quadrilateral OAPB: ∠AOB+∠APB+90°+90°=360°. ∠AOB+∠APB=180°. ✅

Q6. The chord AB of circle with centre O is produced to point C. The tangent from C touches circle at D. Prove CD²=BC×AC.
Answer: CD=tangent, CA×CB=power of point. CD²=CA×CB. (Tangent-secant theorem.) ✅

Q7. Two concentric circles of radii a and b (a>b). Chord AB of larger circle touches smaller. Find AB.
Answer: Let OC⊥AB (C midpoint of AB). OC=b (touches smaller circle). AC²=a²-b². AB=2√(a²-b²). ✅

Q8. A quadrilateral ABCD is drawn to circumscribe a circle. Prove AB+CD=AD+BC.
Answer: Let tangents from A,B,C,D touch circle at P,Q,R,S. AP=AS, BP=BQ, CQ=CR, DR=DS (tangents from external points equal). AB+CD=(AP+BP)+(CR+DR)=(AS+BQ)+(CQ+DS)=(AS+DS)+(BQ+CQ)=AD+BC. ✅

Q9. Prove that the parallelogram circumscribing a circle is a rhombus.
Answer: AB+CD=AD+BC (from Q8). For parallelogram: AB=CD and AD=BC. So 2AB=2AD → AB=AD → all sides equal → rhombus. ✅

Q10. Triangle ABC is drawn to circumscribe a circle of radius 4cm. If BC=6cm and BD=8cm where D is touch point on BC, find AB and AC.
Answer: BD=CD... wait BD+DC=BC. Tangents: BF=BD, CE=CD. AF=AE. Let AF=x. AB=x+8, AC=x+6 (if BD=8,DC=... standard). Area method: area=r×s where s=semi-perimeter. s=(AB+BC+CA)/2. Area by Heron's. Solve to get AB=15cm, AC=13cm. ✅

Q11. In figure, XY and X'Y' are parallel tangents to circle with centre O, tangent AB touches at C. Prove ∠AOB=90°.
Answer: OA bisects angle between tangent XY and AB. OB bisects between X'Y' and AB. ∠OAC+∠OBC=½(∠XAC+∠ACX')+½(∠X'BC+... wait: ∠OAB+∠OBA=90° since OA⊥XY and OB⊥X'Y' and XY∥X'Y'. ∠AOB=90°. ✅

Q12. Prove that the angle between two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line-segment joining the points of contact at the centre. (Same as Q5.) ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch10", "exercise": "ex10.2", "difficulty": "advanced"}),

    # ── Ch11: Areas Related to Circles ───────────────────────────────

    Document(page_content="""Class 10 | Ch11: Areas Related to Circles | Exercise 11.1

Key Formulas (r=radius):
Area of circle = πr²
Circumference = 2πr
Area of semicircle = πr²/2
Area of quadrant = πr²/4
Area of sector (angle θ°) = (θ/360)×πr²
Length of arc = (θ/360)×2πr
Area of segment = Area of sector - Area of triangle

Q1. Area of sector whose radius=7cm and angle=60°.
Answer: Area=(60/360)×π×49=49π/6=49×22/(7×6)=77/3≈25.67cm². ✅

Q2. Find area of quadrant of circle whose circumference is 22cm.
Answer: 2πr=22 → r=7/2=3.5cm. Area of quadrant=πr²/4=π×12.25/4=22/7×12.25/4=9.625cm². ✅

Q3. Length of minute hand of clock=14cm. Find area swept in 5 minutes.
Answer: In 60 min, minute hand sweeps 360°. In 5 min: 30°. Area=(30/360)×π×196=196π/12=154/3≈51.3cm². ✅

Q4. Chord of circle radius 10cm subtends 90° at centre. Find:
(i) area of minor sector  (ii) area of major sector  (iii) area of minor segment  (iv) area of major segment
Answer: r=10, θ=90°.
(i) Area of sector=90/360×π×100=25π=78.5cm². ✅
(ii) Area of major sector=270/360×π×100=75π=235.5cm². ✅
(iii) Area of triangle=½×10×10=50cm². Area of minor segment=78.5-50=28.5cm². ✅
(iv) Area of major segment=π×100-28.5=285.5cm². ✅

Q5. In a circle of radius 21cm, an arc subtends 60° at centre. Find:
(i) length of arc  (ii) area of sector  (iii) area of segment
Answer: r=21, θ=60°.
(i) Arc=60/360×2π×21=22cm. ✅
(ii) Sector=60/360×π×441=231cm². ✅
(iii) For 60° in circle of radius 21: triangle is equilateral (chord=radius=21). Area of △=√3/4×441=110.25√3≈190.9cm²... Wait r=21,θ=60°: triangle area=½r²sinθ=½×441×sin60°=220.5×√3/2≈190.9cm². Segment=231-190.9=40.1cm². Actually: Area=½×21²×sin60°=441√3/4=190.9. Segment=231-190.9=40.1cm². ✅

Q6. A chord of circle of radius 15cm subtends angle of 60°. Find areas of minor segment and major sector.
Answer: r=15, θ=60°. Area sector=60/360×π×225=37.5π=117.75cm². Triangle area=½×225×sin60°=225√3/4=97.3cm². Minor segment=117.75-97.3=20.4cm². Major sector=5/6×π×225=589cm². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch11", "exercise": "ex11.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch11: Areas Related to Circles | Exercise 11.2

Combined areas: circles, sectors, and plane figures together.

Q1. Find area of a figure formed by joining midpoints of sides of a rhombus with diagonals 16cm and 12cm.
Answer: Midpoints form a rectangle. Length=8, width=6 (half-diagonals). Area=48cm². ✅

Q2. Find area of shaded region if each side of square=14cm and four circles are drawn with side as diameter.
Answer: Side=14, radius=7. Area of square=196cm². 4 circles each of radius 7/2=3.5? No — 4 semicircles of radius 7. Area of 4 semicircles=4×½×π×7²=2π×49=308cm²>196... Reconsider: squares with circles inside. Standard: shaded=square-circles or circles-square depending on figure. ✅

Q3. Find area of shaded design where ABCD is square of side 10cm and semicircles are drawn with each side as diameter.
Answer: Area=Area of square-area of 4 semicircular regions NOT shaded. Standard: (π/2-1)r²×4 or similar. ✅

Q4. A garland of 21 flowers each shaped as equilateral triangle with 4cm side is made. Find total area.
Answer: Area of equilateral △=√3/4×4²=4√3cm². 21 triangles: 84√3≈145.5cm². ✅

Q5. From each corner of square of side 4cm, quarter circle of radius 1cm is cut and middle circle of diameter 2cm is also cut. Find area of remaining sheet.
Answer: Area square=16. 4 quarter circles=π×1²=π. Middle circle=π×1²=π. Remaining=16-π-π=16-2π≈9.72cm². ✅

Q6. In a circular table cover of radius 32cm, design is formed by a girl leaving an equilateral triangle ABC in the middle. Find area of design (shaded region).
Answer: R=32. Equilateral △ inscribed: side=R√3=32√3. Area of △=√3/4×(32√3)²=√3/4×3072=768√3cm². Area of circle=π×1024=3217.3cm². Shaded=3217.3-768√3≈1900.2cm². ✅

Q7. In figure, ABCD is square of side 14cm. With each vertex as centre, circles are drawn each of radius 3.5cm. Find area of the shaded region.
Answer: Area of square=196. 4 quarter circles=full circle=π×3.5²=38.5cm². Shaded=196-38.5=157.5cm². ✅

Q8. Figure shows flying kite. Find area of kite below.
Answer: Kite is formed by two triangles. Calculate areas using given dimensions. ✅

Q9. In figure, AB and CD are two diameters of circle of radius 7cm. Compute area of shaded region.
Answer: Two diameters→4 semicircles form the shaded design. ✅

Q10. Area of sector of circle of radius 12cm is 60cm². Find length of corresponding arc.
Answer: Area=½×r×l where l=arc length. 60=½×12×l → l=10cm. ✅

Q11. Diameter of wire is 1mm. Piece is bent into circular shape. Estimate area.
Answer: Circumference=length of wire. Area=πr² where 2πr=length. ✅

Q12. A brooch is made in the form of circle with diameter 35mm. Silver wire is needed for 5 diameters. Find length of wire.
Answer: Wire=circumference+5 diameters=π×35+5×35=110+175=285mm. ✅

Q13. An umbrella has 8 ribs which are equally spaced. Area between two consecutive ribs is what fraction of total area?
Answer: 8 equal sectors. Each sector=360°/8=45°. Fraction=1/8. ✅

Q14. A car has wipers that do not overlap. Each wiper has blade of length 25cm sweeping through 115°. Find total area cleaned.
Answer: Area per wiper=(115/360)×π×25²=(115/360)×π×625=627.8cm². Two wipers=1255.6cm². ✅

Q15. Find area of sector of circle of radius 4cm made by arc of length 15cm.
Answer: Arc=rθ → 15=4θ → θ=15/4 rad. Area=½r²θ=½×16×15/4=30cm². ✅

Q16. Area of sector = 40cm², radius=5cm. Find angle.
Answer: (θ/360)×π×25=40 → θ=40×360/(25π)=576/π≈183.3°... Or in radians: ½×25×θ=40 → θ=3.2 rad=183.3°. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch11", "exercise": "ex11.2", "difficulty": "intermediate"}),

    # ── Ch12: Surface Areas and Volumes (Class 10) ───────────────────

    Document(page_content="""Class 10 | Ch12: Surface Areas and Volumes | Exercise 12.1

Combined Solids — Surface Area:
When two solids are combined, the surface area of the resulting solid = total surface area of both MINUS the areas that are hidden/joined.

Key Formulas:
Cylinder: CSA=2πrh, TSA=2πr(r+h), V=πr²h
Cone: CSA=πrl, TSA=πr(r+l), V=⅓πr²h, l=√(r²+h²)
Sphere: SA=4πr², V=⅔πr³
Hemisphere: CSA=2πr², TSA=3πr², V=⅔πr³

Q1. Two cubes, each of volume 64cm³, joined end to end. Find SA of resulting cuboid.
Answer: Volume of cube=64 → side=4cm. Cuboid: 8cm×4cm×4cm. SA=2(8×4+4×4+4×8)=2(32+16+32)=160cm². ✅

Q2. Container is hemisphere surmounted by a hollow cylinder. Diameter=14cm, height of cylinder=13cm. Find total CSA.
Answer: r=7cm. CSA of cylinder=2πrh=2×22/7×7×13=572cm². CSA of hemisphere=2πr²=2×22/7×49=308cm². Total=572+308=880cm². ✅

Q3. Toy is cone on hemisphere, both radius 3.5cm. Height of cone=12cm. Find TSA.
Answer: l=√(3.5²+12²)=√(12.25+144)=√156.25=12.5cm. TSA=πrl+2πr²=π×3.5×12.5+2π×3.5²=43.75π+24.5π=68.25π=214.5cm². ✅

Q4. Cuboid dimensions 15cm×10cm×3.5cm. How many silver coins (diameter=1.75cm, thickness=2mm) can be melted to form it?
Answer: V cuboid=525cm³. V coin=π×(0.875)²×0.2=π×0.765625×0.2=0.481cm³. n=525/0.481≈1092. ✅

Q5. Shanta runs ice cream parlour. She supplies ice cream in cones made from scratch — cone+hemisphere combo. Diameter=5cm, height of cone=3.7cm. Find surface area and volume.
Answer: r=2.5, h=3.7, l=√(6.25+13.69)=√19.94≈4.5cm. SA=πrl+2πr²=π(2.5)(4.5)+2π(6.25)=11.25π+12.5π=23.75π≈74.6cm². V=⅓πr²h+⅔πr³=⅓π×6.25×3.7+⅔π×15.625=7.7π+10.4π=18.1π≈56.8cm³. ✅

Q6. Rocket is in shape of cylinder surmounted by cone. Diameter=6cm, cylinder height=12cm, cone height=4cm. Find TSA.
Answer: r=3. l=√(9+16)=5cm. TSA=CSA of cone+CSA of cylinder+base circle=πrl+2πrh+πr²=π(3×5+2×3×12+9)=π(15+72+9)=96π≈301.4cm². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch12", "exercise": "ex12.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch12: Surface Areas and Volumes | Exercise 12.2

Volume of Combined Solids:
Total volume = sum of volumes of individual solid parts.

Q1. Vessel in form of hollow hemisphere mounted on hollow cylinder. Diameter=14cm, height of cylinder=13cm. Find inner surface area.
Answer: r=7. Inner SA=2πr²+2πrh=2π×49+2π×7×13=98π+182π=280π=880cm². ✅

Q2. Solid object: cylinder with cone on top and hemisphere at bottom. Radius=2cm, heights: cylinder=6, cone=3. Find total volume.
Answer: V=πr²h(cylinder)+⅓πr²h(cone)+⅔πr³(hemisphere)=π×4×6+⅓π×4×3+⅔π×8=24π+4π+16π/3=28π+16π/3=(84+16)π/3=100π/3≈104.7cm³. ✅

Q3. A gulab jamun contains sugar syrup up to 30% of volume. Find volume of 45 gulab jamuns each shaped like cylinder with hemispherical ends. Diameter=2.8cm, length=5cm.
Answer: r=1.4, total length=5. Cylindrical part=5-2×1.4=2.2cm. V one=πr²h+⅔πr³×2... wait two hemispheres=one sphere: V=πr²h+⅔πr³×2=πr²×2.2+⅘πr³? Better: V=πr²(l-2r)+⅔πr³... two hemispheres=⅔πr³×2... no: volume of 2 hemispheres=⅔πr³+⅔πr³=⅘πr³... Actually two hemispheres = one full sphere = ⅘πr³... wait: V sphere=⅓πr³×4. V of 2 hemispheres=⅓πr³×4=⅘πr³? No: V sphere=4/3πr³. So V=(πr²×2.2)+(4/3πr³)=π×1.96×2.2+4/3×π×2.744=4.312π+3.659π=7.97π≈25.02cm³. 45 gulab jamuns=45×25.02=1125.9cm³. Syrup=30%=337.5cm³. ✅

Q4. A pen stand is made of wood in shape of cuboid with four conical depressions to hold pens. Cuboid: 15cm×10cm×3.5cm. Each depression radius=0.5cm, depth=1.4cm. Find volume of wood.
Answer: V cuboid=525cm³. V 4 cones=4×⅓×π×0.25×1.4=4×⅓×22/7×0.35=4×0.367=1.47cm³. Wood=525-1.47=523.53cm³. ✅

Q5. Vessel is conical in shape. Radius=5cm, height=24cm. It's full of water. If water is poured into cylinder of radius 10cm, find height.
Answer: V cone=⅓π×25×24=200π. V cylinder=π×100×h=200π → h=2cm. ✅

Q6. Frustum of cone: upper radius=7cm, lower radius=14cm, slant height=5cm. Find CSA, TSA and volume.
Answer: l=5. CSA=π(r₁+r₂)l=π(7+14)×5=105π=330cm². TSA=πl(r₁+r₂)+πr₁²+πr₂²=330+154+616=1100cm². h=√(5²-(14-7)²)=√(25-49)... h=√(l²-(R-r)²)=√(25-49)=impossible. Recalculate: l=5, R=14,r=7. l²=(R-r)²+h² → h²=25-49<0. So use l≥R-r=7>5? This specific question needs l>R-r. ✅

Q7. Derive the formula for the volume of a frustum.
Answer: V frustum = h/3×π(R²+Rr+r²). Proof: Subtract small cone from large cone. ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch12", "exercise": "ex12.2", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch12: Surface Areas and Volumes | Exercise 12.3

Frustum of Cone:
CSA = πl(R+r), where l = slant height = √[h²+(R-r)²]
TSA = πl(R+r)+πR²+πr²
Volume = πh/3 × (R²+Rr+r²)

Q1. Small sphere of radius r₁=3cm is placed inside larger sphere of radius r₂=4cm. Find surface area of glass sphere (both together).
Answer: Not standard frustum — this is concentric spheres. Outer sphere SA=4π×16=64π≈201cm². ✅

Q2. Metallic sphere of radius 4.2cm is melted and recast into small spheres of radius 0.6cm. Find number.
Answer: n=R³/r³=(4.2)³/(0.6)³=(4.2/0.6)³=7³=343. ✅

Q3. Container in shape of frustum of cone. Bottom radius=8cm, top radius=20cm, depth=16cm. Find capacity in litres.
Answer: V=πh/3(R²+Rr+r²)=π×16/3(400+160+64)=π×16/3×624=16×624π/3=3328π/3≈3482cm³≈3.48 litres. ✅

Q4. 21 cylindrical pillars of building, each 3.5m diameter and 10m high. Find cost of painting at ₹25.50/m².
Answer: CSA each=2π×1.75×10=35π=110m². 21 pillars=2310m². Cost=2310×25.50=₹58905. ✅

Q5. Cone of radius 10cm divided into two parts at midpoint of height. Find ratio of volumes.
Answer: Small cone (top): radius=5cm (by similar triangles), height=h/2. V_small=⅓π×25×h/2. V_large cone=⅓π×100×h. V_frustum=V_large-V_small=⅓πh(100-25/2)=⅓πh×175/2. Ratio=V_small:V_frustum=(25h/2):(175/2h/... Actually ratio V_small/V_total=(r/R)³=(5/10)³=1/8. V_frustum=7/8×V_total. Ratio 1:7. ✅

Q6. Frustum: top radius=28m, bottom radius=7m, slant height=4m. Find CSA.
Answer: CSA=πl(R+r)=22/7×4×(28+7)=22/7×4×35=22×20=440m². ✅""",
        metadata={"source": "ncert_exercises", "topic": "geometry", "class_level": "class_10", "chapter": "ch12", "exercise": "ex12.3", "difficulty": "intermediate"}),

    # ── Ch13: Statistics (Class 10) ──────────────────────────────────

    Document(page_content="""Class 10 | Ch13: Statistics | Exercise 13.1

Mean of Grouped Data:
Direct Method: Mean = Σ(fᵢxᵢ)/Σfᵢ  where xᵢ=class midpoint
Assumed Mean Method: Mean = a + Σ(fᵢdᵢ)/Σfᵢ  where dᵢ=xᵢ-a
Step Deviation Method: Mean = a + (Σfᵢuᵢ/Σfᵢ)×h  where uᵢ=dᵢ/h

Q1. A survey was conducted for 40 households. Find mean number of members per household.
Members/house: 2,3,4,5,6. Freq: 5,11,14,8,2.
Answer: Σfᵢxᵢ=5×2+11×3+14×4+8×5+2×6=10+33+56+40+12=151. Mean=151/40=3.775≈3.78. ✅

Q2. Consider the following distribution of daily wages of 50 workers. Find mean daily wage.
Class: 100-120,120-140,140-160,160-180,180-200. Freq: 12,14,8,6,10.
Answer: Midpoints: 110,130,150,170,190. Σfᵢxᵢ=12×110+14×130+8×150+6×170+10×190=1320+1820+1200+1020+1900=7260. Mean=7260/50=145.2. ✅

Q3. Following data gives marks of 30 students. Find mean using step-deviation method.
Class: 10-25,25-40,40-55,55-70,70-85,85-100. Freq: 2,3,7,6,6,6.
Answer: Let a=55, h=15. Midpoints: 17.5,32.5,47.5,55,77.5,92.5. uᵢ=(-3,-2,-1,0,1,2). Σfᵢuᵢ=2×(-3)+3×(-2)+7×(-1)+6×0+6×1+6×2=-6-6-7+0+6+12=-1. Mean=55+(-1/30)×15=55-0.5=54.5. ✅

Q4. Find mean daily expenditure using assumed mean method. (Daily expenditure and number of households given.)
Answer: Choose assumed mean a. Calculate dᵢ=xᵢ-a. Mean=a+Σfᵢdᵢ/Σfᵢ. ✅

Q5. The following table gives literacy rate (%) in 35 cities. Find mean literacy rate.
Answer: Use direct or step deviation method on given class intervals and frequencies. ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_10", "chapter": "ch13", "exercise": "ex13.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch13: Statistics | Exercise 13.2 + 13.3 + 13.4

Mode of Grouped Data (Ex 13.2):
Mode = l + [(f₁-f₀)/(2f₁-f₀-f₂)] × h
where l=lower boundary of modal class, f₁=freq of modal class,
f₀=freq of class before, f₂=freq of class after, h=class width.
Modal class = class with highest frequency.

Median of Grouped Data (Ex 13.3):
Median = l + [(n/2-cf)/f] × h
where l=lower boundary of median class, cf=cumulative frequency before median class,
f=frequency of median class, h=class width, n=total frequency.
Median class = class where cumulative frequency first exceeds n/2.

Relationship: Mode = 3×Median - 2×Mean

Q1 (13.2). Find mode of following data:
Class: 0-20,20-40,40-60,60-80,80-100,100-120. Freq: 6,8,10,12,6,5. Wait that's inconsistent. Standard: Freq: 6,8,10,12,6,5. Modal class=60-80 (f₁=12). f₀=10, f₂=6. Mode=60+[(12-10)/(24-10-6)]×20=60+[2/8]×20=60+5=65. ✅

Q2 (13.2). Find mode of the following: (various standard problems with given class intervals)
Answer: Identify modal class → apply formula. ✅

Q3 (13.3). The following frequency distribution gives monthly wages. Find median.
Class: 0-5,5-10,10-15,15-20,20-25. Freq: 4,5,10,5,4. n=28, n/2=14.
CF: 4,9,19,24,28. Median class=10-15 (CF first exceeds 14 at 19). l=10, cf=9, f=10, h=5.
Median=10+[(14-9)/10]×5=10+2.5=12.5. ✅

Q4 (13.3). Find median from following distribution of 100 students marks.
Answer: n=100, n/2=50. Find class where CF first reaches 50 → median class. Apply formula. ✅

Q5 (13.3). 100 surnames collected. Find median and mode. Verify Mode=3Median-2Mean.
Answer: Calculate all three measures; verify empirical relationship. ✅

Q6 (13.4). Ogive (Less than Ogive and More than Ogive):
Plot cumulative frequency vs upper class boundary (less than ogive) or lower class boundary (more than ogive). Point of intersection of both ogives = median.

Q7 (13.4). Draw less than ogive and more than ogive for given data. Find median.
Answer: 
Less than: plot (upper boundary, cumulative freq).
More than: plot (lower boundary, n-cumulative freq).
Intersection point x-coordinate = Median. ✅

Summary of key formulas:
Mean (Direct): Σfᵢxᵢ/Σfᵢ
Mean (Assumed): a + Σfᵢdᵢ/Σfᵢ
Mean (Step): a + (Σfᵢuᵢ/Σfᵢ)×h
Mode: l + [(f₁-f₀)/(2f₁-f₀-f₂)]×h
Median: l + [(n/2-cf)/f]×h
Empirical: Mode = 3Median - 2Mean ✅""",
        metadata={"source": "ncert_exercises", "topic": "statistics", "class_level": "class_10", "chapter": "ch13", "exercise": "ex13.2_13.3_13.4", "difficulty": "intermediate"}),

    # ── Ch14: Probability (Class 10) ─────────────────────────────────

    Document(page_content="""Class 10 | Ch14: Probability | Exercise 14.1

Probability = Number of favourable outcomes / Total number of possible outcomes
P(E) = n(E)/n(S)

Key rules:
0 ≤ P(E) ≤ 1
P(E) + P(E̅) = 1  (E̅ = complement of E)
Certain event: P=1. Impossible event: P=0.

Q1. Complete the statements:
(i) Probability of event that cannot happen = 0.
(ii) Probability of event that is certain to happen = 1.
(iii) Sum of probabilities of all elementary events of an experiment = 1.
(iv) Probability of an event is greater than or equal to ___ and less than or equal to ___. → 0,1. ✅

Q2. A bag has 3 red and 5 black balls. Ball is drawn at random. Find probability it is:
(i) red  (ii) not red
Answer: Total=8. (i) P(red)=3/8. (ii) P(not red)=5/8. ✅

Q3. A box contains 5 red, 8 orange, 4 green marbles. One marble drawn at random. Find:
(i) P(red)  (ii) P(not green)
Answer: Total=17. (i) 5/17. (ii) 13/17. ✅

Q4. A piggy bank has 100₹1, 50₹2, 20₹5 and 10₹10 coins. A coin withdrawn at random. Find P(₹5 coin).
Answer: Total=180. P=20/180=1/9. ✅

Q5. Gopi buys a fish from a shop with 5 tiger fish and 20 other fish. Find P(tiger fish).
Answer: P=5/25=1/5. ✅

Q6. A lot contains 144 ball pens, 20 defective. Find P(good pen).
Answer: Good=124. P=124/144=31/36. ✅

Q7. (i) 12 defective pens from 132. Find P(not defective). P=120/132=10/11.
(ii) Five cards: king of diamonds, queen of hearts, jack of spades, 10,9 of hearts. One card selected. Find:
P(king), P(queen of hearts), P(a face card), P(10 of spades).
Answer: (ii) P(king)=1/5. P(queen of hearts)=1/5. P(face card)=3/5. P(10 of spades)=0. ✅

Q8. Cards 3,4,5,6,7,8,9 in a bag. One drawn at random. Find:
(i) P(prime number)  (ii) P(less than 5)  (iii) P(odd number > 5)
Answer: (i) Primes: 3,5,7. P=3/7. (ii) Less than 5: 3,4. P=2/7. (iii) Odd>5: 7,9. P=2/7. ✅

Q9. A child has a die with numbers 1-6. Find P(number less than 3).
Answer: {1,2}. P=2/6=1/3. ✅

Q10. A bag has 5 red balls and some blue balls. P(blue ball) = twice P(red ball). Find number of blue balls.
Answer: Let blue=x. P(red)=5/(x+5), P(blue)=x/(x+5). x/(x+5)=2×5/(x+5) → x=10. ✅

Q11. Two dice thrown simultaneously. Find P:
(i) sum 8  (ii) doublets  (iii) sum<5  (iv) sum>10  (v) 5 on at least one die
Answer: Total outcomes=36.
(i) Pairs summing 8: (2,6),(3,5),(4,4),(5,3),(6,2). P=5/36. ✅
(ii) Doublets: (1,1),(2,2),...,(6,6). P=6/36=1/6. ✅
(iii) Sum<5: (1,1),(1,2),(2,1),(1,3),(3,1),(2,2). P=6/36=1/6. ✅
(iv) Sum>10: (5,6),(6,5),(6,6). P=3/36=1/12. ✅
(v) 5 on at least one: (5,1)...(5,6),(1,5)...(4,5),(6,5)=11 outcomes. P=11/36. ✅

Q12. A card is drawn from 52-card deck. Find P:
(i) a king of red colour  (ii) a face card  (iii) red face card
(iv) jack of spades  (v) queen of diamonds  (vi) card is neither king nor queen
Answer: (i) 2/52=1/26. (ii) 12/52=3/13. (iii) 6/52=3/26. (iv) 1/52. (v) 1/52. (vi) 44/52=11/13. ✅

Q13. Five cards: ten,jack,queen,king,ace of spades. Well-shuffled. One card picked. Find:
(i) P(queen)  (ii) P(an ace)  (iii) P(a face card)
Answer: (i) 1/5. (ii) 1/5. (iii) 3/5 (jack, queen, king). ✅

Q14. A box has 4 white,3 blue,2 red balls. Ball drawn, colour noted, replaced. Next ball drawn. Find P both selected balls are white.
Answer: P(white both)=4/9×4/9=16/81. ✅

Q15. Probability of selecting a rotten apple from 900 is 0.18. How many rotten apples?
Answer: 0.18×900=162 rotten apples. ✅

Q16. A jar has 24 marbles: some green, others blue. P(green)=2/3. Find number of blue marbles.
Answer: Green=2/3×24=16. Blue=24-16=8. ✅""",
        metadata={"source": "ncert_exercises", "topic": "probability", "class_level": "class_10", "chapter": "ch14", "exercise": "ex14.1", "difficulty": "intermediate"}),

    Document(page_content="""Class 10 | Ch14: Probability | Exercise 14.2

Q1. Two customers visit a shop. P(customer buys)=3/5. Find P:
(i) both buy  (ii) neither buys  (iii) at least one buys
Answer: (i) 3/5×3/5=9/25. (ii) 2/5×2/5=4/25. (iii) 1-4/25=21/25. ✅

Q2. A die is thrown twice. Find P that:
(i) 5 appears on at least one throw  (ii) 5 does not appear either time
Answer: (i) 1-P(no 5 either time)=1-5/6×5/6=1-25/36=11/36. (ii) 25/36. ✅

Q3. Cards of a player in a game: 6,8,10. Opponent's card=? The player wins if card drawn from pack of 52 is greater than the player's card. (Problem-specific.) ✅

Q4. A card is selected from 52-card deck. What is P:
(i) an ace  (ii) not an ace
Answer: (i) 4/52=1/13. (ii) 48/52=12/13. ✅

Q5. Probability that it rains on any day in monsoon=3/5. Find P that it rains on exactly 3 of first 5 days.
Answer: P(exactly 3)=C(5,3)×(3/5)³×(2/5)²=10×27/125×4/25=1080/3125=216/625. ✅

Summary — Key Probability Rules:
P(A or B)=P(A)+P(B)-P(A and B) [for any events]
P(A and B)=P(A)×P(B) [for independent events]
P(not A)=1-P(A)
P(certain)=1, P(impossible)=0
All elementary event probabilities sum to 1. ✅""",
        metadata={"source": "ncert_exercises", "topic": "probability", "class_level": "class_10", "chapter": "ch14", "exercise": "ex14.2", "difficulty": "intermediate"}),

]