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

]

