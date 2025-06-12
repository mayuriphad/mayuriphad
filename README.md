"use client"

import type React from "react"

import { useState, useEffect, useRef } from "react"
import { motion, useAnimation, useInView } from "framer-motion"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  Mail,
  Github,
  Linkedin,
  Code,
  Database,
  Brain,
  Trophy,
  Star,
  GitBranch,
  Zap,
  Heart,
  Coffee,
  Rocket,
  Target,
  BookOpen,
  Award,
  Sparkles,
  ExternalLink,
  Flame,
} from "lucide-react"

// Custom hook for animation when element comes into view
const useAnimateInView = () => {
  const ref = useRef(null)
  const isInView = useInView(ref, { once: false, margin: "-100px" })
  const controls = useAnimation()

  useEffect(() => {
    if (isInView) {
      controls.start("visible")
    }
  }, [isInView, controls])

  return {
    ref,
    controls,
    variants: {
      hidden: { opacity: 0, y: 75 },
      visible: { opacity: 1, y: 0, transition: { duration: 0.8 } },
    },
  }
}

const TypewriterText = ({ text, delay = 0 }: { text: string; delay?: number }) => {
  const [displayText, setDisplayText] = useState("")
  const [currentIndex, setCurrentIndex] = useState(0)

  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentIndex < text.length) {
        setDisplayText((prev) => prev + text[currentIndex])
        setCurrentIndex((prev) => prev + 1)
      }
    }, 100 + delay)

    return () => clearTimeout(timer)
  }, [currentIndex, text, delay])

  return (
    <span className="relative">
      {displayText}
      <motion.span
        animate={{ opacity: [1, 0, 1] }}
        transition={{ duration: 1, repeat: Number.POSITIVE_INFINITY }}
        className="text-cyan-400 absolute"
      >
        |
      </motion.span>
    </span>
  )
}

const FloatingIcon = ({
  children,
  delay = 0,
  glowColor = "cyan",
}: {
  children: React.ReactNode
  delay?: number
  glowColor?: string
}) => {
  const glowClasses = {
    cyan: "drop-shadow-[0_0_15px_rgba(6,182,212,0.7)]",
    purple: "drop-shadow-[0_0_15px_rgba(168,85,247,0.7)]",
    pink: "drop-shadow-[0_0_15px_rgba(236,72,153,0.7)]",
    yellow: "drop-shadow-[0_0_15px_rgba(250,204,21,0.7)]",
  }

  return (
    <motion.div
      initial={{ y: 0 }}
      animate={{ y: [-15, 15, -15] }}
      transition={{
        duration: 4,
        repeat: Number.POSITIVE_INFINITY,
        delay,
        ease: "easeInOut",
      }}
      className="relative"
    >
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ duration: 8, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
        className={glowClasses[glowColor as keyof typeof glowClasses]}
      >
        {children}
      </motion.div>
    </motion.div>
  )
}

const AnimatedCard = ({
  children,
  delay = 0,
  className = "",
}: { children: React.ReactNode; delay?: number; className?: string }) => {
  const { ref, controls, variants } = useAnimateInView()

  return (
    <motion.div
      ref={ref}
      initial="hidden"
      animate={controls}
      variants={variants}
      whileHover={{
        scale: 1.02,
        boxShadow: "0 25px 50px rgba(6,182,212,0.2)",
      }}
      className={className}
    >
      {children}
    </motion.div>
  )
}

const SkillBadge = ({
  skill,
  icon,
  delay = 0,
  color = "cyan",
}: { skill: string; icon: React.ReactNode; delay?: number; color?: string }) => {
  const colorClasses = {
    cyan: "from-cyan-500/30 to-blue-500/30 border-cyan-500/50 hover:border-cyan-400 hover:shadow-cyan-400/40",
    purple: "from-purple-500/30 to-pink-500/30 border-purple-500/50 hover:border-purple-400 hover:shadow-purple-400/40",
    green: "from-green-500/30 to-emerald-500/30 border-green-500/50 hover:border-green-400 hover:shadow-green-400/40",
    orange: "from-orange-500/30 to-red-500/30 border-orange-500/50 hover:border-orange-400 hover:shadow-orange-400/40",
  }

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5, delay }}
      whileHover={{
        scale: 1.1,
        y: -5,
        transition: { duration: 0.2 },
      }}
      whileTap={{ scale: 0.95 }}
    >
      <Badge
        variant="outline"
        className={`flex items-center gap-2 p-3 bg-gradient-to-r ${colorClasses[color as keyof typeof colorClasses]} border text-white hover:shadow-lg transition-all duration-300 text-sm font-medium`}
      >
        {icon}
        {skill}
      </Badge>
    </motion.div>
  )
}

const ParticleBackground = () => {
  return (
    <div className="fixed inset-0 overflow-hidden pointer-events-none z-0">
      {[...Array(80)].map((_, i) => (
        <motion.div
          key={i}
          className={`absolute w-1 h-1 rounded-full ${
            i % 3 === 0 ? "bg-cyan-400" : i % 3 === 1 ? "bg-purple-400" : "bg-pink-400"
          }`}
          initial={{
            x: Math.random() * window.innerWidth,
            y: Math.random() * window.innerHeight,
            opacity: 0,
            scale: Math.random() * 0.5 + 0.5,
          }}
          animate={{
            y: [null, Math.random() > 0.5 ? "-100vh" : "100vh"],
            opacity: [0, 1, 0],
            scale: [Math.random() * 0.5 + 0.5, Math.random() * 1 + 1, Math.random() * 0.5 + 0.5],
          }}
          transition={{
            duration: Math.random() * 10 + 10,
            repeat: Number.POSITIVE_INFINITY,
            delay: Math.random() * 5,
            ease: "linear",
          }}
        />
      ))}
    </div>
  )
}

const GlowingBorder = ({ children, color = "cyan" }: { children: React.ReactNode; color?: string }) => {
  const borderColors = {
    cyan: "border-cyan-500/50 shadow-[0_0_15px_rgba(6,182,212,0.3)]",
    purple: "border-purple-500/50 shadow-[0_0_15px_rgba(168,85,247,0.3)]",
    pink: "border-pink-500/50 shadow-[0_0_15px_rgba(236,72,153,0.3)]",
    yellow: "border-yellow-500/50 shadow-[0_0_15px_rgba(250,204,21,0.3)]",
  }

  return <div className={`border ${borderColors[color as keyof typeof borderColors]} rounded-xl p-1`}>{children}</div>
}

const PulsingIcon = ({ icon, color = "text-cyan-400" }: { icon: React.ReactNode; color?: string }) => {
  return (
    <motion.div
      animate={{
        scale: [1, 1.2, 1],
        opacity: [0.7, 1, 0.7],
      }}
      transition={{
        duration: 2,
        repeat: Number.POSITIVE_INFINITY,
        ease: "easeInOut",
      }}
      className={`${color}`}
    >
      {icon}
    </motion.div>
  )
}

const StarRating = ({ count = 5 }: { count?: number }) => {
  return (
    <div className="flex space-x-1">
      {[...Array(count)].map((_, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0, scale: 0 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: i * 0.1, duration: 0.3 }}
        >
          <motion.div
            animate={{
              scale: [1, 1.3, 1],
              rotate: [0, i % 2 === 0 ? 5 : -5, 0],
            }}
            transition={{
              duration: 2 + i * 0.2,
              repeat: Number.POSITIVE_INFINITY,
              delay: i * 0.2,
            }}
          >
            <Star className="w-5 h-5 text-yellow-400 fill-yellow-400" />
          </motion.div>
        </motion.div>
      ))}
    </div>
  )
}

export default function AnimatedProfile() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    setIsVisible(true)
  }, [])

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.3,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 },
  }

  return (
    <div className="min-h-screen bg-black relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-black">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,182,212,0.08),transparent_50%)]" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(168,85,247,0.08),transparent_50%)]" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_80%,rgba(236,72,153,0.08),transparent_50%)]" />
      </div>

      <ParticleBackground />

      <motion.div
        className="container mx-auto px-4 py-8 relative z-10"
        variants={containerVariants}
        initial="hidden"
        animate={isVisible ? "visible" : "hidden"}
      >
        {/* Hero Section */}
        <motion.div className="text-center mb-16" variants={itemVariants}>
          <motion.div
            initial={{ scale: 0, rotate: -180 }}
            animate={{ scale: 1, rotate: 0 }}
            transition={{ duration: 1.2, type: "spring", bounce: 0.6 }}
            className="mb-8"
          >
            <div className="w-40 h-40 mx-auto bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500 rounded-full flex items-center justify-center text-7xl mb-6 relative">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 20, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
                className="absolute inset-0 rounded-full border-4 border-dashed border-cyan-400/50"
              />
              <motion.div
                animate={{ rotate: -360 }}
                transition={{ duration: 15, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
                className="absolute inset-2 rounded-full border-4 border-dotted border-purple-400/50"
              />
              <motion.span
                animate={{
                  scale: [1, 1.2, 1],
                  rotateY: [0, 360],
                }}
                transition={{
                  scale: { duration: 2, repeat: Number.POSITIVE_INFINITY },
                  rotateY: { duration: 5, repeat: Number.POSITIVE_INFINITY },
                }}
                className="relative z-10"
              >
                👋
              </motion.span>
            </div>
          </motion.div>

          <motion.h1
            className="text-6xl md:text-7xl font-bold bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent mb-6"
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
          >
            Hi, I'm Mayuri Phad
          </motion.h1>

          <motion.h3
            className="text-3xl text-gray-100 mb-8"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.8 }}
          >
            <TypewriterText text="An aspiring Machine Learning enthusiast!" delay={1000} />
          </motion.h3>

          <motion.div
            className="flex justify-center gap-8"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2 }}
          >
            <FloatingIcon delay={0} glowColor="cyan">
              <Brain className="w-12 h-12 text-cyan-400" />
            </FloatingIcon>
            <FloatingIcon delay={0.5} glowColor="purple">
              <Code className="w-12 h-12 text-purple-400" />
            </FloatingIcon>
            <FloatingIcon delay={1} glowColor="pink">
              <Rocket className="w-12 h-12 text-pink-400" />
            </FloatingIcon>
          </motion.div>
        </motion.div>

        {/* About Me Section */}
        <AnimatedCard delay={0.2}>
          <Card className="mb-12 border border-cyan-500/30 shadow-2xl bg-black backdrop-blur-xl">
            <CardContent className="p-10">
              <motion.h2
                className="text-4xl font-bold mb-8 flex items-center gap-4 text-white"
                variants={itemVariants}
                initial={{ x: -50, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                transition={{ duration: 0.8 }}
              >
                <Rocket className="w-10 h-10 text-cyan-400" />
                About Me
                <motion.div
                  animate={{
                    rotate: [0, 10, -10, 0],
                    scale: [1, 1.2, 1],
                  }}
                  transition={{ duration: 3, repeat: Number.POSITIVE_INFINITY }}
                >
                  <Sparkles className="w-6 h-6 text-yellow-400" />
                </motion.div>
              </motion.h2>
              <div className="grid md:grid-cols-2 gap-8">
                <motion.div className="space-y-6" variants={itemVariants}>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-blue-500/10 to-cyan-500/10 border border-blue-500/30 hover:border-blue-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(6,182,212,0.3)",
                      x: 5,
                    }}
                  >
                    <Target className="w-6 h-6 text-blue-400" />
                    <span className="text-gray-100 text-lg">
                      Currently exploring <strong className="text-cyan-400">Machine Learning</strong>
                    </span>
                  </motion.div>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-green-500/10 to-emerald-500/10 border border-green-500/30 hover:border-green-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(34,197,94,0.3)",
                      x: 5,
                    }}
                  >
                    <BookOpen className="w-6 h-6 text-green-400" />
                    <span className="text-gray-100 text-lg">
                      Learning <strong className="text-green-400">Deep Learning</strong> and{" "}
                      <strong className="text-emerald-400">AI Model Optimization</strong>
                    </span>
                  </motion.div>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-pink-500/10 to-purple-500/10 border border-pink-500/30 hover:border-pink-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(236,72,153,0.3)",
                      x: 5,
                    }}
                  >
                    <Mail className="w-6 h-6 text-pink-400" />
                    <span className="text-gray-100 text-lg">
                      Reach me: <strong className="text-pink-400">mayuriphad5@gmail.com</strong>
                    </span>
                  </motion.div>
                </motion.div>
                <motion.div className="space-y-6" variants={itemVariants}>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-purple-500/10 to-pink-500/10 border border-purple-500/30 hover:border-purple-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(168,85,247,0.3)",
                      x: 5,
                    }}
                  >
                    <Heart className="w-6 h-6 text-purple-400" />
                    <span className="text-gray-100 text-lg">
                      Pronouns: <strong className="text-purple-400">She/Her</strong>
                    </span>
                  </motion.div>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 hover:border-yellow-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(234,179,8,0.3)",
                      x: 5,
                    }}
                  >
                    <Zap className="w-6 h-6 text-yellow-400" />
                    <span className="text-gray-100 text-lg">
                      Love working on <strong className="text-yellow-400">AI-powered projects</strong>
                    </span>
                  </motion.div>
                  <motion.div
                    className="flex items-center gap-4 p-4 rounded-xl bg-gradient-to-r from-indigo-500/10 to-blue-500/10 border border-indigo-500/30 hover:border-indigo-400/60 transition-all duration-300"
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 20px rgba(99,102,241,0.3)",
                      x: 5,
                    }}
                  >
                    <Coffee className="w-6 h-6 text-indigo-400" />
                    <span className="text-gray-100 text-lg">
                      Experimenting with <strong className="text-indigo-400">ML architectures</strong>
                    </span>
                  </motion.div>
                </motion.div>
              </div>
            </CardContent>
          </Card>
        </AnimatedCard>

        {/* Achievements Section - Enhanced with animations */}
        <AnimatedCard delay={0.4}>
          <Card className="mb-12 border border-yellow-500/30 shadow-2xl bg-black backdrop-blur-xl overflow-hidden">
            <CardContent className="p-10 relative">
              {/* Animated background elements */}
              <div className="absolute inset-0 overflow-hidden">
                {[...Array(15)].map((_, i) => (
                  <motion.div
                    key={i}
                    className="absolute w-1 h-20 bg-gradient-to-b from-yellow-400/0 via-yellow-400/20 to-yellow-400/0"
                    style={{
                      left: `${Math.random() * 100}%`,
                      top: `${Math.random() * 100}%`,
                      rotate: `${Math.random() * 90}deg`,
                    }}
                    animate={{
                      opacity: [0, 0.5, 0],
                      y: [0, 100],
                    }}
                    transition={{
                      duration: Math.random() * 5 + 5,
                      repeat: Number.POSITIVE_INFINITY,
                      delay: Math.random() * 5,
                    }}
                  />
                ))}
              </div>

              <motion.h2
                className="text-4xl font-bold mb-8 flex items-center gap-4 text-white relative z-10"
                variants={itemVariants}
                initial={{ x: -50, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                transition={{ duration: 0.8 }}
              >
                <motion.div
                  animate={{
                    rotate: [0, 10, -10, 0],
                    scale: [1, 1.2, 1],
                  }}
                  transition={{ duration: 3, repeat: Number.POSITIVE_INFINITY }}
                >
                  <Trophy className="w-10 h-10 text-yellow-400" />
                </motion.div>
                Notable Achievements
                <motion.div
                  animate={{
                    scale: [1, 1.3, 1],
                    rotate: [0, 360],
                  }}
                  transition={{
                    scale: { duration: 2, repeat: Number.POSITIVE_INFINITY },
                    rotate: { duration: 8, repeat: Number.POSITIVE_INFINITY, ease: "linear" },
                  }}
                >
                  <Star className="w-6 h-6 text-yellow-400" />
                </motion.div>
              </motion.h2>

              <GlowingBorder color="yellow">
                <motion.div
                  className="flex items-center gap-6 p-8 bg-black rounded-xl border border-yellow-500/30 hover:border-yellow-400/50 transition-all duration-300 relative overflow-hidden"
                  whileHover={{
                    scale: 1.02,
                    boxShadow: "0 0 30px rgba(234,179,8,0.3)",
                  }}
                >
                  {/* Animated background for achievement card */}
                  <div className="absolute inset-0 overflow-hidden">
                    <motion.div
                      className="absolute inset-0 bg-gradient-to-r from-yellow-500/5 to-orange-500/5"
                      animate={{
                        backgroundPosition: ["0% 0%", "100% 100%"],
                      }}
                      transition={{
                        duration: 10,
                        repeat: Number.POSITIVE_INFINITY,
                        repeatType: "reverse",
                      }}
                    />
                  </div>

                  <motion.div
                    animate={{
                      rotate: [0, 360],
                      scale: [1, 1.2, 1],
                    }}
                    transition={{
                      rotate: { duration: 20, repeat: Number.POSITIVE_INFINITY, ease: "linear" },
                      scale: { duration: 3, repeat: Number.POSITIVE_INFINITY },
                    }}
                    className="relative"
                  >
                    <Award className="w-20 h-20 text-yellow-400 drop-shadow-[0_0_15px_rgba(234,179,8,0.7)]" />
                    <motion.div
                      className="absolute inset-0 rounded-full"
                      animate={{
                        boxShadow: ["0 0 0 0px rgba(234,179,8,0.3)", "0 0 0 10px rgba(234,179,8,0)"],
                      }}
                      transition={{
                        duration: 2,
                        repeat: Number.POSITIVE_INFINITY,
                      }}
                    />
                  </motion.div>

                  <div className="relative z-10">
                    <motion.p
                      className="text-2xl font-bold text-white mb-3"
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.3 }}
                    >
                      Published ML research in{" "}
                      <motion.span
                        className="text-yellow-400"
                        animate={{
                          textShadow: [
                            "0 0 5px rgba(234,179,8,0.5)",
                            "0 0 20px rgba(234,179,8,0.8)",
                            "0 0 5px rgba(234,179,8,0.5)",
                          ],
                        }}
                        transition={{ duration: 2, repeat: Number.POSITIVE_INFINITY }}
                      >
                        IEEE conferences
                      </motion.span>
                    </motion.p>

                    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5 }}>
                      <div className="flex flex-wrap gap-3 mb-4">
                        {["Drowsiness Detection", "Medicinal Plant Identification", "Violence Detection"].map(
                          (topic, i) => (
                            <motion.span
                              key={topic}
                              className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${
                                i === 0
                                  ? "bg-cyan-500/20 text-cyan-300 border border-cyan-500/40"
                                  : i === 1
                                    ? "bg-green-500/20 text-green-300 border border-green-500/40"
                                    : "bg-pink-500/20 text-pink-300 border border-pink-500/40"
                              }`}
                              initial={{ opacity: 0, scale: 0 }}
                              animate={{ opacity: 1, scale: 1 }}
                              transition={{ delay: 0.6 + i * 0.2 }}
                              whileHover={{ scale: 1.05 }}
                            >
                              {topic}
                            </motion.span>
                          ),
                        )}
                      </div>

                      <div className="flex items-center gap-2">
                        <StarRating count={5} />
                        <span className="text-gray-300 text-sm">Top-rated research papers</span>
                      </div>
                    </motion.div>
                  </div>
                </motion.div>
              </GlowingBorder>
            </CardContent>
          </Card>
        </AnimatedCard>

        {/* Tech Stack Section */}
        <AnimatedCard delay={0.6}>
          <Card className="mb-12 border border-purple-500/30 shadow-2xl bg-black backdrop-blur-xl">
            <CardContent className="p-10">
              <motion.h2
                className="text-4xl font-bold mb-8 flex items-center gap-4 text-white"
                variants={itemVariants}
                initial={{ x: -50, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                transition={{ duration: 0.8 }}
              >
                <Code className="w-10 h-10 text-purple-400" />
                Tech Stack
                <motion.div
                  animate={{
                    scale: [1, 1.2, 1],
                    rotate: [0, 5, -5, 0],
                  }}
                  transition={{ duration: 2, repeat: Number.POSITIVE_INFINITY }}
                >
                  <Sparkles className="w-6 h-6 text-purple-400" />
                </motion.div>
              </motion.h2>

              <div className="space-y-8">
                <div>
                  <h3 className="text-2xl font-semibold mb-6 flex items-center gap-3 text-cyan-400">
                    <PulsingIcon icon={<Code className="w-6 h-6" />} />
                    Languages & Frameworks
                  </h3>
                  <div className="flex flex-wrap gap-4">
                    {[
                      { name: "Python", icon: <Code className="w-4 h-4" />, color: "cyan" },
                      { name: "C/C++", icon: <Code className="w-4 h-4" />, color: "purple" },
                      { name: "Java", icon: <Code className="w-4 h-4" />, color: "orange" },
                      { name: "JavaScript", icon: <Code className="w-4 h-4" />, color: "green" },
                      { name: "TensorFlow", icon: <Brain className="w-4 h-4" />, color: "cyan" },
                      { name: "Keras", icon: <Brain className="w-4 h-4" />, color: "purple" },
                      { name: "OpenCV", icon: <Brain className="w-4 h-4" />, color: "green" },
                      { name: "React.js", icon: <Code className="w-4 h-4" />, color: "cyan" },
                      { name: "Node.js", icon: <Code className="w-4 h-4" />, color: "green" },
                    ].map((skill, index) => (
                      <SkillBadge
                        key={skill.name}
                        skill={skill.name}
                        icon={skill.icon}
                        delay={index * 0.1}
                        color={skill.color}
                      />
                    ))}
                  </div>
                </div>

                <div>
                  <h3 className="text-2xl font-semibold mb-6 flex items-center gap-3 text-green-400">
                    <PulsingIcon icon={<Database className="w-6 h-6" />} color="text-green-400" />
                    Databases & Tools
                  </h3>
                  <div className="flex flex-wrap gap-4">
                    {[
                      { name: "MySQL", icon: <Database className="w-4 h-4" />, color: "cyan" },
                      { name: "MongoDB", icon: <Database className="w-4 h-4" />, color: "green" },
                      { name: "Git", icon: <GitBranch className="w-4 h-4" />, color: "orange" },
                      { name: "GitHub", icon: <Github className="w-4 h-4" />, color: "purple" },
                      { name: "VSCode", icon: <Code className="w-4 h-4" />, color: "cyan" },
                    ].map((skill, index) => (
                      <SkillBadge
                        key={skill.name}
                        skill={skill.name}
                        icon={skill.icon}
                        delay={index * 0.1}
                        color={skill.color}
                      />
                    ))}
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </AnimatedCard>

        {/* GitHub Stats Section - Enhanced with animations */}
        <AnimatedCard delay={0.8}>
          <Card className="mb-12 border border-cyan-500/30 shadow-2xl bg-black backdrop-blur-xl">
            <CardContent className="p-10">
              <motion.h2
                className="text-4xl font-bold mb-8 flex items-center gap-4 text-white"
                variants={itemVariants}
                initial={{ x: -50, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                transition={{ duration: 0.8 }}
              >
                <motion.div
                  animate={{
                    rotate: [0, 360],
                    scale: [1, 1.2, 1],
                  }}
                  transition={{
                    rotate: { duration: 10, repeat: Number.POSITIVE_INFINITY, ease: "linear" },
                    scale: { duration: 3, repeat: Number.POSITIVE_INFINITY },
                  }}
                >
                  <Star className="w-10 h-10 text-cyan-400" />
                </motion.div>
                GitHub Stats
                <motion.div
                  animate={{
                    rotate: [0, 360],
                    scale: [1, 1.2, 1],
                  }}
                  transition={{
                    rotate: { duration: 8, repeat: Number.POSITIVE_INFINITY, ease: "linear" },
                    scale: { duration: 2, repeat: Number.POSITIVE_INFINITY },
                  }}
                >
                  <Github className="w-6 h-6 text-cyan-400" />
                </motion.div>
              </motion.h2>

              <div className="grid md:grid-cols-2 gap-8">
                <GlowingBorder color="cyan">
                  <motion.div
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 30px rgba(6,182,212,0.3)",
                      y: -5,
                    }}
                    className="bg-black p-6 rounded-xl border border-cyan-500/30 hover:border-cyan-400/50 transition-all duration-300 relative overflow-hidden"
                  >
                    {/* Animated background for stats card */}
                    <div className="absolute inset-0 overflow-hidden">
                      <motion.div
                        className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 to-blue-500/5"
                        animate={{
                          backgroundPosition: ["0% 0%", "100% 100%"],
                        }}
                        transition={{
                          duration: 8,
                          repeat: Number.POSITIVE_INFINITY,
                          repeatType: "reverse",
                        }}
                      />
                    </div>

                    <motion.div
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.3 }}
                      className="relative z-10"
                    >
                      <img
                        src="https://github-readme-stats.vercel.app/api?username=mayuriphad&show_icons=true&theme=radical"
                        alt="GitHub Stats"
                        className="w-full rounded-lg"
                      />
                    </motion.div>

                    {/* Animated stars */}
                    <div className="absolute top-2 right-2 z-20">
                      <StarRating count={3} />
                    </div>
                  </motion.div>
                </GlowingBorder>

                <GlowingBorder color="purple">
                  <motion.div
                    whileHover={{
                      scale: 1.03,
                      boxShadow: "0 0 30px rgba(168,85,247,0.3)",
                      y: -5,
                    }}
                    className="bg-black p-6 rounded-xl border border-purple-500/30 hover:border-purple-400/50 transition-all duration-300 relative overflow-hidden"
                  >
                    {/* Animated background for stats card */}
                    <div className="absolute inset-0 overflow-hidden">
                      <motion.div
                        className="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-pink-500/5"
                        animate={{
                          backgroundPosition: ["0% 0%", "100% 100%"],
                        }}
                        transition={{
                          duration: 8,
                          repeat: Number.POSITIVE_INFINITY,
                          repeatType: "reverse",
                        }}
                      />
                    </div>

                    <motion.div
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.5 }}
                      className="relative z-10"
                    >
                      <img
                        src="https://github-readme-streak-stats.herokuapp.com/?user=mayuriphad&theme=radical"
                        alt="GitHub Streak"
                        className="w-full rounded-lg"
                      />
                    </motion.div>

                    {/* Animated stars */}
                    <div className="absolute top-2 right-2 z-20">
                      <StarRating count={3} />
                    </div>
                  </motion.div>
                </GlowingBorder>
              </div>

              <GlowingBorder color="yellow" className="mt-8">
                <motion.div
                  className="mt-8 bg-black p-6 rounded-xl border border-yellow-500/30 hover:border-yellow-400/50 transition-all duration-300 relative overflow-hidden"
                  whileHover={{
                    scale: 1.02,
                    boxShadow: "0 0 30px rgba(234,179,8,0.3)",
                    y: -5,
                  }}
                >
                  {/* Animated background for trophies card */}
                  <div className="absolute inset-0 overflow-hidden">
                    <motion.div
                      className="absolute inset-0 bg-gradient-to-br from-yellow-500/5 to-orange-500/5"
                      animate={{
                        backgroundPosition: ["0% 0%", "100% 100%"],
                      }}
                      transition={{
                        duration: 8,
                        repeat: Number.POSITIVE_INFINITY,
                        repeatType: "reverse",
                      }}
                    />

                    {/* Trophy animations */}
                    {[...Array(5)].map((_, i) => (
                      <motion.div
                        key={i}
                        className="absolute"
                        style={{
                          left: `${20 + i * 15}%`,
                          top: "-20px",
                        }}
                        animate={{
                          y: [0, 5, 0],
                          opacity: [0.3, 0.6, 0.3],
                        }}
                        transition={{
                          duration: 2 + i * 0.5,
                          repeat: Number.POSITIVE_INFINITY,
                          delay: i * 0.3,
                        }}
                      >
                        <Trophy className="w-6 h-6 text-yellow-400/30" />
                      </motion.div>
                    ))}
                  </div>

                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.7 }}
                    className="relative z-10"
                  >
                    <img
                      src="https://github-profile-trophy.vercel.app/?username=mayuriphad&theme=radical"
                      alt="GitHub Trophies"
                      className="w-full rounded-lg"
                    />
                  </motion.div>

                  {/* Animated stars */}
                  <div className="absolute top-2 right-2 z-20">
                    <StarRating count={5} />
                  </div>
                </motion.div>
              </GlowingBorder>
            </CardContent>
          </Card>
        </AnimatedCard>

        {/* Connect Section - Enhanced with animations */}
        <AnimatedCard delay={1.0}>
          <Card className="border border-cyan-500/30 shadow-2xl bg-black backdrop-blur-xl relative overflow-hidden">
            {/* Animated background elements */}
            <div className="absolute inset-0 overflow-hidden">
              <motion.div
                className="absolute inset-0 bg-gradient-to-r from-cyan-500/10 via-purple-500/10 to-pink-500/10"
                animate={{
                  backgroundPosition: ["0% 0%", "100% 100%"],
                }}
                transition={{
                  duration: 15,
                  repeat: Number.POSITIVE_INFINITY,
                  repeatType: "reverse",
                }}
              />

              {/* Animated particles */}
              {[...Array(20)].map((_, i) => (
                <motion.div
                  key={i}
                  className="absolute w-1 h-1 rounded-full bg-cyan-400"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                  }}
                  animate={{
                    scale: [0, 1.5, 0],
                    opacity: [0, 0.8, 0],
                  }}
                  transition={{
                    duration: Math.random() * 3 + 2,
                    repeat: Number.POSITIVE_INFINITY,
                    delay: Math.random() * 5,
                  }}
                />
              ))}
            </div>

            <CardContent className="p-12 text-center relative z-10">
              <motion.h2
                className="text-5xl font-bold mb-8 text-white"
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
              >
                <motion.span
                  className="inline-block"
                  animate={{
                    textShadow: [
                      "0 0 5px rgba(6,182,212,0.5)",
                      "0 0 20px rgba(6,182,212,0.8)",
                      "0 0 5px rgba(6,182,212,0.5)",
                    ],
                  }}
                  transition={{ duration: 3, repeat: Number.POSITIVE_INFINITY }}
                >
                  Let's Connect & Collaborate!
                </motion.span>
                <motion.div
                  animate={{
                    y: [0, -15, 0],
                    rotate: [0, 10, -10, 0],
                  }}
                  transition={{ duration: 2, repeat: Number.POSITIVE_INFINITY }}
                  className="inline-block ml-4"
                >
                  <Flame className="w-10 h-10 text-orange-400" />
                </motion.div>
              </motion.h2>

              <motion.div
                className="flex flex-wrap justify-center gap-6 mb-10"
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.3 }}
              >
                <motion.a
                  href="https://www.linkedin.com/in/mayuriphad/"
                  whileHover={{
                    scale: 1.1,
                    y: -8,
                    boxShadow: "0 20px 30px rgba(6,182,212,0.4)",
                  }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    size="lg"
                    className="flex items-center gap-3 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 border border-blue-500/50 text-white shadow-lg hover:shadow-blue-500/25 transition-all duration-300 text-lg px-6 py-6"
                  >
                    <motion.div
                      animate={{ rotate: [0, 360] }}
                      transition={{ duration: 5, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
                    >
                      <Linkedin className="w-6 h-6" />
                    </motion.div>
                    LinkedIn
                    <motion.div
                      animate={{ x: [0, 5, 0] }}
                      transition={{ duration: 1, repeat: Number.POSITIVE_INFINITY }}
                    >
                      <ExternalLink className="w-5 h-5" />
                    </motion.div>
                  </Button>
                </motion.a>

                <motion.a
                  href="https://github.com/mayuriphad"
                  whileHover={{
                    scale: 1.1,
                    y: -8,
                    boxShadow: "0 20px 30px rgba(0,0,0,0.4)",
                  }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    size="lg"
                    className="flex items-center gap-3 bg-gradient-to-r from-gray-700 to-gray-800 hover:from-gray-600 hover:to-gray-700 border border-gray-500/50 text-white shadow-lg hover:shadow-gray-500/25 transition-all duration-300 text-lg px-6 py-6"
                  >
                    <motion.div
                      animate={{ rotate: [0, 360] }}
                      transition={{ duration: 5, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
                    >
                      <Github className="w-6 h-6" />
                    </motion.div>
                    GitHub
                    <motion.div
                      animate={{ x: [0, 5, 0] }}
                      transition={{ duration: 1, repeat: Number.POSITIVE_INFINITY }}
                    >
                      <ExternalLink className="w-5 h-5" />
                    </motion.div>
                  </Button>
                </motion.a>

                <motion.a
                  href="mailto:mayuriphad5@gmail.com"
                  whileHover={{
                    scale: 1.1,
                    y: -8,
                    boxShadow: "0 20px 30px rgba(236,72,153,0.4)",
                  }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    size="lg"
                    className="flex items-center gap-3 bg-gradient-to-r from-pink-600 to-pink-700 hover:from-pink-500 hover:to-pink-600 border border-pink-500/50 text-white shadow-lg hover:shadow-pink-500/25 transition-all duration-300 text-lg px-6 py-6"
                  >
                    <motion.div
                      animate={{ rotate: [0, 360] }}
                      transition={{ duration: 5, repeat: Number.POSITIVE_INFINITY, ease: "linear" }}
                    >
                      <Mail className="w-6 h-6" />
                    </motion.div>
                    Email
                    <motion.div
                      animate={{ x: [0, 5, 0] }}
                      transition={{ duration: 1, repeat: Number.POSITIVE_INFINITY }}
                    >
                      <ExternalLink className="w-5 h-5" />
                    </motion.div>
                  </Button>
                </motion.a>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.6 }}
              >
                <motion.p
                  className="text-2xl font-bold"
                  animate={{
                    color: [
                      "rgb(34,211,238)", // cyan-400
                      "rgb(168,85,247)", // purple-500
                      "rgb(236,72,153)", // pink-500
                      "rgb(34,211,238)", // back to cyan-400
                    ],
                  }}
                  transition={{ duration: 8, repeat: Number.POSITIVE_INFINITY }}
                >
                  🔥 Thanks for visiting my profile! Let's build amazing ML projects together! 🔥
                </motion.p>
              </motion.div>
            </CardContent>
          </Card>
        </AnimatedCard>
      </motion.div>
    </div>
  )
}
